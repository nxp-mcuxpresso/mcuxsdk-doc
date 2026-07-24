"""
merge_example_readmes — post-copy Sphinx extension.

After external_content copies example readmes into the Sphinx source tree (it
connects `sync_contents` to `builder-inited`), this runs on the same event at a
LOWER priority (higher number => later) and merges, per example:

    examples/<cat>/<ex>/readme.md                     (common example readme)
      + each board's linked example_board_readme.md   (board-specific setup)

into ONE example doc. Board setups are placed behind a single board SELECTOR
(a dropdown that shows one board's setup at a time) so it scales cleanly from 1
to 100+ boards (e.g. hello_world has ~91). The standalone per-board readme files
are removed from the (generated) source tree so they are not built as separate
pages — collapsing the per-board flood.

Merge key: the common readme's "Supported Boards" section links to each board's
example_board_readme.md. Everything happens in the build src dir (DOCS_SRC_DIR);
the original mcuxsdk/examples sources and the standalone SDK package are never
touched.

Enable: add "merge_example_readmes" to the extensions list.
"""
from __future__ import annotations
import os
import re
import shutil
from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx

_BOARD_LINK = re.compile(
    r"\[([^\]]+)\]\(([^)]*_boards/([^/]+)/[^)]*example_board_readme\.md)\)")
_SUPPORTED_HDR = re.compile(r"^\s{0,3}#{1,6}\s*Supported\s+Boards\s*$", re.I | re.M)
_ATX = re.compile(r"^(#{1,6})(\s+.*)$", re.M)
_MD_IMG = re.compile(r"(!\[[^\]]*\]\()([^)]+?)(\s+\"[^\"]*\")?\)")

# Injected once per page (no-op where there is no .board-selector). Builds a
# <select> from the board setups, shows one at a time.
_SELECTOR_JS = r"""
(function () {
  function init() {
    var style = document.createElement('style');
    style.textContent =
      '.board-select-label{display:block;margin:1rem 0 .5rem;font-weight:600}' +
      '.board-select{margin-left:.5rem;padding:.25rem .5rem;max-width:100%}' +
      '.board-setup{border-left:3px solid var(--pst-color-primary,#0a5aa5);padding-left:1rem}';
    document.head.appendChild(style);
    var saved = null;
    try { saved = localStorage.getItem('mcux_board'); } catch (e) {}
    document.querySelectorAll('.board-selector').forEach(function (group) {
      var setups = group.querySelectorAll('.board-setup');
      if (!setups.length) return;
      var sel = document.createElement('select');
      sel.className = 'board-select';
      var defaultIdx = 0;
      var savedId = saved ? ('board-' + saved) : null;
      setups.forEach(function (s, i) {
        var h = s.querySelector('h1,h2,h3,h4,h5,h6');
        var name = h ? h.textContent.replace(/[#¶]/g, '').trim() : s.id;
        if (h) h.style.display = 'none';
        var opt = document.createElement('option');
        opt.value = s.id; opt.textContent = name;
        sel.appendChild(opt);
        if (savedId && s.id === savedId) defaultIdx = i;  // pre-select persisted board
      });
      setups.forEach(function (s, i) { s.style.display = (i === defaultIdx) ? 'block' : 'none'; });
      sel.selectedIndex = defaultIdx;
      sel.addEventListener('change', function () {
        setups.forEach(function (s) {
          s.style.display = (s.id === sel.value) ? 'block' : 'none';
        });
        try { localStorage.setItem('mcux_board', sel.value.replace(/^board-/, '')); } catch (e) {}
      });
      var label = document.createElement('label');
      label.className = 'board-select-label';
      label.textContent = 'Board setup for: ';
      label.appendChild(sel);
      group.insertBefore(label, group.firstChild);
    });
  }
  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
"""


def _demote_headings(text: str, by: int = 4) -> str:
    lines = text.splitlines()
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if line.strip() and re.match(r"^\s*=+\s*$", nxt):
            out.append("#" * min(6, 1 + by) + " " + line.strip()); i += 2; continue
        if line.strip() and re.match(r"^\s*-{2,}\s*$", nxt):
            out.append("#" * min(6, 2 + by) + " " + line.strip()); i += 2; continue
        m = _ATX.match(line)
        out.append("#" * min(6, len(m.group(1)) + by) + m.group(2) if m else line)
        i += 1
    return "\n".join(out)


def _rewrite_images(body: str, board_md: Path, common_dir: Path, slug: str) -> str:
    def repl(m):
        pre, path, title = m.group(1), m.group(2).strip(), m.group(3) or ""
        if path.startswith(("http://", "https://", "/", "data:")):
            return m.group(0)
        src = (board_md.parent / path).resolve()
        if not src.is_file():
            return m.group(0)
        rel = f"_board_images/{slug}/{src.name}"
        dst = common_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copy(src, dst)
        except OSError:
            return m.group(0)
        return f"{pre}{rel}{title})"
    return _MD_IMG.sub(repl, body)


# Markdown links (not images): [text](target) — target captured with an
# optional #fragment. Images are handled separately by _rewrite_images.
_MD_LINK = re.compile(r"(?<!\!)(\[[^\]]*\]\()([^)\s#]+)(#[^)\s]*)?(\))")


def _rewrite_links(body: str, board_md: Path, common_dir: Path,
                   srcdir: Path = None, sdk_base: Path = None) -> str:
    """Re-express relative links for the merged location.

    Board readmes are written relative to their _boards/<b>/<cat>/<ex>/ home
    so they render on GitHub/IDE; merged into examples/<cat>/<ex>/readme.md
    those paths re-root wrongly. Recompute each relative target from the
    board file's real location and re-relativize it to the merged page.
    Links to other example_board_readme.md files (merged away) point at the
    owning example's merged readme instead.

    Existence is checked in the build srcdir first, then in the SDK workspace
    (``sdk_base``): source files (.c/.cmake/.icf, ...) served by the
    source_pages extension live only in the workspace — they are never copied
    into the srcdir mirror — yet their links must still be re-rooted so the
    source_pages domain can match them against its whitelist after merging.
    """
    def _target_exists(target: Path) -> bool:
        if target.exists():
            return True
        if srcdir is not None and sdk_base is not None:
            try:
                rel = target.relative_to(srcdir)
            except ValueError:
                return False
            return (sdk_base / rel).exists()
        return False

    def repl(m):
        pre, path, frag, close = m.group(1), m.group(2), m.group(3) or "", m.group(4)
        if path.startswith(("http://", "https://", "mailto:", "/", "data:")):
            return m.group(0)
        target = (board_md.parent / path).resolve()
        try:
            if target.name == "example_board_readme.md":
                # merged into its example's readme: link that page instead
                parts = target.parts
                i = parts.index("_boards")
                ex_root = Path(*parts[:i])                # .../examples
                ex_rel = Path(*parts[i + 2:-1])           # <cat>/<ex>[/variant]
                merged = ex_root / ex_rel / "readme.md"
                # variant dirs (cm33/...) roll up to the example readme
                while not merged.is_file() and len(ex_rel.parts) > 1:
                    ex_rel = ex_rel.parent
                    merged = ex_root / ex_rel / "readme.md"
                if merged.is_file():
                    rel = os.path.relpath(merged, common_dir)
                    return f"{pre}{Path(rel).as_posix()}{frag}{close}"
            if _target_exists(target):
                rel = os.path.relpath(target, common_dir)
                return f"{pre}{Path(rel).as_posix()}{frag}{close}"
        except (ValueError, OSError):
            pass
        return m.group(0)
    return _MD_LINK.sub(repl, body)


def _max_backtick_run(texts):
    longest = 0
    for t in texts:
        for run in re.findall(r"`+", t):
            longest = max(longest, len(run))
    return longest


def _example_of_board_md(rel: str) -> str:
    """Example-relative path a board readme belongs to.

    "../../_boards/<board>/eiq_examples/tflm_label_image/example_board_readme.md"
    -> "eiq_examples/tflm_label_image".
    """
    parts = rel.replace("\\", "/").split("/")
    try:
        i = parts.index("_boards")
    except ValueError:
        return ""
    return "/".join(parts[i + 2: -1])


def _merge_one(readme: Path, ex_root: Path, to_delete: set,
               srcdir: Path = None, sdk_base: Path = None):
    text = readme.read_text(encoding="utf-8", errors="ignore")
    m = _SUPPORTED_HDR.search(text)
    if not m:
        return False, 0
    head = text[: m.start()].rstrip()
    links = _BOARD_LINK.findall(text[m.start():])
    if not links:
        return False, 0

    common_dir = readme.parent
    own_example = readme.parent.relative_to(ex_root).as_posix()
    boards = []
    removed = 0
    seen_boards = set()
    for name, rel, bdir in links:
        board_md = (common_dir / rel).resolve()
        if not board_md.is_file():
            continue                    # board filtered out of this build
        # Key the board section by the board DIRECTORY (e.g. "frdmk22f") so it
        # matches the persisted selection from the Examples Catalog.
        slug = bdir.strip()
        # Board variants (e.g. IMX952LPD5EVK-19 / -15) may list the same
        # board readme more than once; merge each unique file once, or the
        # repeated ":name: board-<slug>" containers emit docutils
        # "Duplicate explicit target name" warnings.
        if (slug, board_md) in seen_boards:
            continue
        seen_boards.add((slug, board_md))
        body = board_md.read_text(encoding="utf-8", errors="ignore").strip()
        body = _rewrite_images(body, board_md, common_dir, slug)
        body = _rewrite_links(body, board_md, common_dir, srcdir, sdk_base)
        boards.append((name, slug, _demote_headings(body)))
        # Only the OWNING example's board readme is deleted, and deletion is
        # deferred until every readme has merged (merges only read _boards
        # files, so readme writes never interfere). Cross-example consumers
        # (variant examples reusing another example's board readme, or several
        # examples sharing one board file) merge a copy and leave the file, so
        # plain links from readmes that never merge still resolve.
        if _example_of_board_md(rel) == own_example:
            to_delete.add(board_md); removed += 1
    if not boards:
        return False, 0

    maxrun = _max_backtick_run([b for _, _, b in boards])
    inner = "`" * max(3, maxrun + 1)     # board-setup container fence
    outer = "`" * max(4, maxrun + 2)     # board-selector group fence

    # Keep the "Supported Boards" heading text: its per-document slug
    # (#supported-boards) is a common self-link target in readme prose, and
    # heading slugs don't register global labels (a "(supported-boards)="
    # target here would duplicate across every merged readme).
    parts = [head, "", "## Supported Boards", "",
             f"{outer}{{container}} board-selector", ""]
    slug_counts: dict = {}
    for name, slug, body in boards:
        # Same board with several core/variant readmes (e.g. imx943evk
        # cm33_core1/cm7_core0/...): container names must stay unique per
        # document or docutils warns "Duplicate explicit target name".
        n = slug_counts.get(slug, 0) + 1
        slug_counts[slug] = n
        anchor = f"board-{slug}" if n == 1 else f"board-{slug}-{n}"
        parts += [
            f"{inner}{{container}} board-setup",
            f":name: {anchor}",
            "",
            f"##### {name}",
            "",
            body,
            "",
            inner,
            "",
        ]
    parts += [outer, ""]
    readme.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return True, removed


def merge_examples(app: Sphinx) -> None:
    if not app.config.merge_example_readmes:
        return
    ex_root = Path(app.srcdir) / "examples"
    if not ex_root.is_dir():
        return
    merged, removed = 0, 0
    to_delete: set = set()
    for readme in ex_root.rglob("readme.md"):
        if "_boards" in readme.parts:
            continue
        did, r = _merge_one(readme, ex_root, to_delete,
                            srcdir=Path(app.srcdir),
                            sdk_base=Path(app.confdir).parents[0])
        if did:
            merged += 1; removed += r
    for board_md in to_delete:
        try:
            board_md.unlink()
        except OSError:
            pass
    print(f"[merge_example_readmes] merged {merged} example docs; "
          f"folded in / removed {len(to_delete)} standalone board readmes")


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("merge_example_readmes", True, "env")
    app.connect("builder-inited", merge_examples, priority=900)
    app.add_js_file(None, body=_SELECTOR_JS)
    return {"version": "0.3", "parallel_read_safe": True, "parallel_write_safe": True}
