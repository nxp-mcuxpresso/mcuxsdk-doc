"""
mcux_search — build-time search index generation (Pagefind).

On build-finished (html builder only), this extension:
  1. annotates the rendered OUTPUT tree with Pagefind attributes according to
     _cfg/search_config.yml:
       - data-pagefind-ignore on excluded path prefixes (per-board example
         copies, per-device API docs),
       - board-tier weights + landing boosts + board-name alias spans
         (tiers/names from MIR board_status),
       - middleware landing boosts + alias spans (components from the manifest
         middleware division),
       - hub-page boosts and reference-subtree down-weights;
  2. runs the Pagefind CLI over the output tree, producing html/pagefind/.

The search UI lives in _templates/search.html (phrase-aware re-ranking there).
Requires pip packages `pagefind` AND `pagefind_bin`. If the indexer or a data
source (MIR, manifests) is unavailable the build still succeeds — the step is
skipped with a warning and the search page falls back to native search.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict

import yaml
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

ART_OPEN = re.compile(r'(<article\b[^>]*class="[^"]*bd-article[^"]*"[^>]*?)(>)', re.I)
_W_ATTR = re.compile(r'\s*data-pagefind-(?:weight="[0-9.]+"|ignore)')
_ALIAS = re.compile(r'<span class="pf-alias"[^>]*>.*?</span>', re.S)


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _aliases(n: str):
    out = {n}
    for p in ("evkb", "evkc", "evk9", "evk"):
        if n.startswith(p):
            out.add(n[len(p):] + p)
        if n.endswith(p):
            out.add(p + n[:-len(p)])
    return out


def _annotate(page: Path, weight: str | None = None, ignore: bool = False,
              alias: str | None = None) -> bool:
    """Idempotently (re)write pagefind attributes on a page's article tag."""
    try:
        s = page.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    s2 = _ALIAS.sub("", _W_ATTR.sub("", s))
    attr = ' data-pagefind-ignore' if ignore else (
        f' data-pagefind-weight="{weight}"' if weight else "")
    new = ART_OPEN.sub(lambda m: m.group(1) + attr + m.group(2), s2, count=1)
    if alias and not ignore:
        span = (f'<span class="pf-alias" data-pagefind-weight="10" '
                f'style="display:none">{alias}</span>')
        new = ART_OPEN.sub(lambda m: m.group(0) + span, new, count=1)
    if new != s:
        page.write_text(new, encoding="utf-8")
        return True
    return False


def _board_status(mir: Path):
    """Parse MIR board_status -> ({norm alias: tier}, {norm alias: marketing name})."""
    lines = mir.read_text(encoding="utf-8", errors="ignore").splitlines()
    start = next((i + 1 for i, l in enumerate(lines)
                  if re.match(r"\s*board_status:\s*$", l)), None)
    tiers, names = {}, {}
    if start is None:
        return tiers, names
    base = len(lines[start]) - len(lines[start].lstrip())
    for l in lines[start:]:
        if not l.strip():
            continue
        if len(l) - len(l.lstrip()) < base:
            break
        m = re.match(r"\s*([^:]+):\s*'?([A-Za-z]+)'?\s*$", l)
        if m:
            for a in _aliases(_norm(m.group(1))):
                tiers.setdefault(a, m.group(2))
                names.setdefault(a, m.group(1).strip())
    return tiers, names


def _mw_components(mdir: Path):
    """Manifest middleware division -> [(site subpath, display name)]."""
    out = []
    for f in sorted(mdir.glob("*.yml")):
        try:
            d = yaml.safe_load(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for p in (d.get("manifest", {}).get("projects") or []):
            path = (p.get("path") or "").replace("mcuxsdk/", "", 1)
            disp = (p.get("userdata") or {}).get("display_name") or p.get("name", "")
            if path.startswith("middleware/"):
                out.append((path[len("middleware/"):], disp))
    return out


def _annotate_tree(out: Path, cfg: dict, sdk_base: Path) -> None:
    stats: Dict[str, int] = {}

    # 1. excluded path prefixes
    n = 0
    for prefix in cfg.get("exclude_paths", []):
        root = out / prefix
        if root.is_dir():
            for p in root.rglob("*.html"):
                n += _annotate(p, ignore=True)
    stats["excluded"] = n

    # 2. board pages (tiers + landing boosts + aliases from MIR)
    tiers, names = {}, {}
    mir = sdk_base / cfg.get("mir_release_config", "")
    if mir.is_file():
        tiers, names = _board_status(mir)
    else:
        logger.warning("mcux_search: MIR config not found (%s); board weights use Legacy", mir)
    bw = cfg.get("board_weights", {})
    lw = cfg.get("board_landing_weights", {})
    n = 0
    boards_root = out / "boards"
    if boards_root.is_dir():
        for p in boards_root.rglob("*.html"):
            rel = p.relative_to(boards_root).as_posix().split("/")
            if len(rel) < 3:
                continue  # family/root index pages stay neutral
            board = rel[1]
            tier = next((tiers[a] for a in _aliases(_norm(board)) if a in tiers), "Legacy")
            if len(rel) == 3 and rel[2] == "index.html":
                mk = next((names[a] for a in _aliases(_norm(board)) if a in names), None)
                alias = " ".join(dict.fromkeys(filter(None, [board, mk])))
                n += _annotate(p, weight=lw.get(tier, "2"), alias=alias)
            else:
                n += _annotate(p, weight=bw.get(tier, "0.2"))
    stats["boards"] = n

    # 3. middleware landings (manifest division + extras)
    n = 0
    mdir = sdk_base.parent / "manifests" / "submanifests" / "middleware"
    mw_w = str(cfg.get("middleware_landing_weight", "7"))
    if mdir.is_dir():
        for sub, disp in _mw_components(mdir):
            page = out / "middleware" / sub / "index.html"
            if page.is_file():
                dirname = sub.rstrip("/").split("/")[-1]
                alias = " ".join(dict.fromkeys(filter(None, [dirname, disp])))
                n += _annotate(page, weight=mw_w, alias=alias)
    else:
        logger.warning("mcux_search: middleware manifests not found (%s)", mdir)
    for rel, alias in (cfg.get("middleware_extras") or {}).items():
        page = out / rel
        if page.is_file():
            n += _annotate(page, weight=mw_w, alias=str(alias))
    stats["middleware"] = n

    # 4. hub pages and down-weighted subtrees
    n = 0
    for rel, w in (cfg.get("hub_pages") or {}).items():
        page = out / rel
        if page.is_file():
            n += _annotate(page, weight=str(w))
    stats["hubs"] = n
    n = 0
    for prefix, w in (cfg.get("subtree_weights") or {}).items():
        root = out / prefix
        if root.is_dir():
            for p in root.rglob("*.html"):
                n += _annotate(p, weight=str(w))
    stats["subtrees"] = n

    logger.info("mcux_search: annotated %s", stats)


def build_search_index(app: Sphinx, exception) -> None:
    if exception or app.builder.name != "html":
        return
    if not app.config.mcux_search_enable:
        return
    confdir = Path(app.confdir)
    cfg_file = confdir / "_cfg" / "search_config.yml"
    if not cfg_file.is_file():
        logger.warning("mcux_search: _cfg/search_config.yml missing; skipping index")
        return
    cfg = yaml.safe_load(cfg_file.read_text(encoding="utf-8")) or {}
    out = Path(app.outdir)
    sdk_base = confdir.parent

    _annotate_tree(out, cfg, sdk_base)

    bundle = out / "pagefind"
    if bundle.is_dir():
        shutil.rmtree(bundle)
    cmd = [sys.executable, "-m", "pagefind", "--site", str(out),
           "--root-selector", cfg.get("root_selector", ".bd-article"),
           "--force-language", cfg.get("force_language", "en")]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
    except (OSError, subprocess.TimeoutExpired) as e:
        logger.warning("mcux_search: pagefind failed to run (%s); search page will "
                       "fall back to native search", e)
        return
    if res.returncode != 0:
        logger.warning("mcux_search: pagefind exited %d: %s", res.returncode,
                       (res.stderr or res.stdout)[-800:])
        return
    for line in (res.stdout or "").splitlines():
        if "Indexed" in line or "Finished" in line:
            logger.info("mcux_search: %s", line.strip())


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("mcux_search_enable", True, "env")
    app.connect("build-finished", build_search_index)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
