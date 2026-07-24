"""
examples_catalog — build-time filterable Examples Catalog.

On builder-inited (after external_content copies sources), this extension:
  1. reads every common example.yml under <SDK_BASE>/examples (name, brief,
     category, boards),
  2. maps board dir -> family from <DOC_BASE>/boards/<FAMILY>/<board>,
  3. loads the category taxonomy from _cfg/examples_catalog.yml (middleware
     groups follow the manifest middleware division),
  4. embeds the catalog data + config as JSON into examples/index and renders a
     client-side filter UI (pick board family + board -> demos/applications by
     category, with descriptions from example.yml). The chosen board is stored
     in localStorage and pre-selects the board on each merged example page.

Enable: add "examples_catalog" to the extensions list.
"""
from __future__ import annotations
import json
import re
import yaml
from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx

_CONTAINER_ID = "mcux-examples-catalog"


def _families(doc_base: Path) -> Dict[str, str]:
    fam = {}
    root = doc_base / "boards"
    if root.is_dir():
        for f in root.iterdir():
            if f.is_dir():
                for b in f.iterdir():
                    if b.is_dir():
                        fam[b.name] = f.name
    return fam


def _collect(sdk_base: Path, families: Dict[str, str]):
    exroot = sdk_base / "examples"
    catalog = []
    for yml in exroot.rglob("example.yml"):
        if "_boards" in yml.parts:
            continue
        try:
            data = yaml.safe_load(yml.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        rel = yml.parent.relative_to(exroot).as_posix()
        for ex_name, ex in data.items():
            if not isinstance(ex, dict):
                continue
            doc = (ex.get("contents") or {}).get("document") or {}
            bmap = ex.get("boards") or {}
            dirs = sorted({re.split(r"@", b)[0] for b in bmap.keys()})
            if not dirs:
                continue
            # Link target = the common readme from document.example_readme (the
            # example.yml folder is NOT always where the readme lives, e.g.
            # usb .../<variant>/example.yml but readme at the parent).
            readmes = doc.get("example_readme") or []
            common = next((r for r in readmes
                           if isinstance(r, str) and r.startswith("examples/") and r.endswith(".md")), None)
            if common and (sdk_base / common).is_file():
                href = common[len("examples/"):-len(".md")] + ".html"
            elif (exroot / rel / "readme.md").is_file():
                href = rel + "/readme.html"
            else:
                # No doc page (e.g. bootloader examples): a dead card is worse
                # than no card - skip the example entirely.
                continue
            if not any(d in families for d in dirs):
                continue    # no supported board in the documented board set
            catalog.append({
                "name": ex_name,
                "brief": (doc.get("brief") or "").strip(),
                "category": doc.get("category", rel.split("/")[0]),
                "path": rel,
                "href": href,
                "board_count": len(dirs),
                "boards": [{"dir": d, "family": families.get(d, "Other")} for d in dirs],
            })
    return catalog


def build_catalog(app: Sphinx) -> None:
    doc_base = Path(app.confdir)
    sdk_base = doc_base.parent
    if not (sdk_base / "examples").is_dir():
        return
    index = Path(app.srcdir) / "examples" / "index.rst"
    if not index.is_file():
        return
    text = index.read_text(encoding="utf-8", errors="ignore")
    if _CONTAINER_ID in text:
        return  # already injected this build

    try:
        cfg = yaml.safe_load((doc_base / "_cfg" / "examples_catalog.yml").read_text(encoding="utf-8")) or {}
    except Exception:
        cfg = {}
    examples = _collect(sdk_base, _families(doc_base))
    payload = {
        "group_order": cfg.get("group_order", []),
        "pinned": cfg.get("pinned", []),
        "categories": cfg.get("categories", {}),
        "examples": examples,
    }
    data_json = json.dumps(payload, ensure_ascii=True)
    block = (
        ".. raw:: html\n\n"
        f'   <script id="mcux-catalog-data" type="application/json">{data_json}</script>\n'
        f'   <div id="{_CONTAINER_ID}">Loading examples…</div>\n\n'
    )
    cats = payload["categories"] or {}
    order = payload["group_order"] or []

    def _cat_of(entry):
        path = re.search(r"<([^>]+)>", entry)
        path = path.group(1) if path else entry
        return path.split("/")[0]

    def _label(c):
        lg = cats.get(c)
        return lg[0] if isinstance(lg, (list, tuple)) and lg else c

    def _group(c):
        lg = cats.get(c)
        return lg[1] if isinstance(lg, (list, tuple)) and len(lg) > 1 else "Other"

    # Card-driven navigation: strip the toctree from the index page so
    # neither the page body nor the sidebar lists the category indexes.
    # All examples/** docs are orphan-patched via conf.py _ORPHAN_PATTERNS.
    m = re.search(r"^\.\. toctree::", text, re.M)
    if m:
        text = text[:m.start()].rstrip() + "\n\n" + block
    else:
        text = text + "\n\n" + block
    index.write_text(text, encoding="utf-8")

    # Give category index pages readable titles (raw folder names like
    # "driver_examples" otherwise show up in the toctree/sidebar). Sphinx uses a
    # doc's first section title for the toctree link, so retitling fixes the
    # examples index list, the left nav, the breadcrumb and the page heading.
    ex_src = Path(app.srcdir) / "examples"
    title_re = re.compile(r'^([^\n]+)\n([#=*^"~+.\-]{3,})[ \t]*$', re.M)
    retitled = 0
    for cat, lg in (payload["categories"] or {}).items():
        label = (lg[0] if isinstance(lg, (list, tuple)) and lg else None)
        idx = ex_src / cat / "index.rst"
        if not label or not idx.is_file():
            continue
        t = idx.read_text(encoding="utf-8", errors="ignore")
        tm = title_re.search(t)
        if not tm or tm.group(1).strip() == label:
            continue
        ch = tm.group(2)[0]
        t = t[:tm.start()] + f"{label}\n{ch * max(len(label), 3)}" + t[tm.end():]
        idx.write_text(t, encoding="utf-8")
        retitled += 1
    print(f"[examples_catalog] injected catalog with {len(examples)} examples; "
          f"retitled {retitled} category index pages")


_CATALOG_JS = r"""
(function () {
  function init() {
    var host = document.getElementById('mcux-examples-catalog');
    var data = document.getElementById('mcux-catalog-data');
    if (!host || !data) return;
    var D; try { D = JSON.parse(data.textContent); } catch (e) { host.textContent = 'Catalog data error.'; return; }
    var CAT = D.categories || {}, ORDER = D.group_order || [], PINNED = D.pinned || [], EX = D.examples || [];
    var LS = 'mcux_board';

    var css = document.createElement('style');
    css.textContent =
      '#mcux-examples-catalog .cat-filters{display:flex;flex-wrap:wrap;gap:.6rem;align-items:end;margin:1rem 0;padding:.8rem;border:1px solid #d7dee7;border-radius:8px;background:#f6f8fb}' +
      '#mcux-examples-catalog .cf{display:flex;flex-direction:column;gap:.2rem}' +
      '#mcux-examples-catalog .cf label{font-size:.7rem;text-transform:uppercase;letter-spacing:.04em;color:#5b6b7c;font-weight:700}' +
      '#mcux-examples-catalog select,#mcux-examples-catalog input{padding:.4rem .5rem;border:1px solid #d7dee7;border-radius:6px;font-size:.9rem;min-width:160px}' +
      '#mcux-examples-catalog .cat-count{color:#5b6b7c;font-size:.9rem;margin:.4rem 0}' +
      '#mcux-examples-catalog .cat-group{margin:1.4rem 0 .4rem;font-weight:800;color:#0a5aa5;border-bottom:2px solid #0a5aa5;padding-bottom:.3rem;display:flex;justify-content:space-between;align-items:baseline}' +
      '#mcux-examples-catalog .cat-group .n{font-size:.75rem;color:#5b6b7c;font-weight:500}' +
      '#mcux-examples-catalog .cat-sub{margin:.9rem 0 .35rem;font-weight:700;color:#2a3b4d}' +
      '#mcux-examples-catalog .cat-sub .n{font-weight:500;color:#5b6b7c;font-size:.8rem;margin-left:.4rem}' +
      '#mcux-examples-catalog .cat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:.55rem}' +
      '#mcux-examples-catalog .cat-card{border:1px solid #d7dee7;border-radius:8px;padding:.6rem .8rem;background:#fff}' +
      '#mcux-examples-catalog .cat-card a{font-weight:700;text-decoration:none;color:#0a5aa5}' +
      '#mcux-examples-catalog .cat-card .nolink{font-weight:700;color:#5b6b7c}' +
      '#mcux-examples-catalog .cat-card .b{font-size:.83rem;color:#33465a;margin-top:.2rem}' +
      '#mcux-examples-catalog .cat-card .b.none{color:#9aa7b4;font-style:italic}';
    document.head.appendChild(css);

    var uniq = function (a) { return Array.from(new Set(a)).sort(); };
    var meta = function (c) { var t = (c || '').split('/')[0]; return CAT[t] || [t.replace(/_/g, ' ') || 'Other', 'Other']; };
    var preview = function (b) { if (!b) return ''; var m = b.match(/^[\s\S]*?[.!?](\s|$)/); var s = (m ? m[0] : b).trim(); return s.length > 170 ? s.slice(0, 167) + '…' : s; };
    function pinRank(n) { var i = PINNED.indexOf(n); return i < 0 ? 9999 : i; }

    host.innerHTML =
      '<div class="cat-filters">' +
      '<div class="cf"><label>Board family</label><select id="cat-fam"></select></div>' +
      '<div class="cf"><label>Board</label><select id="cat-board"></select></div>' +
      '<div class="cf"><label>Keyword</label><input id="cat-q" placeholder="e.g. i2c, hello, usb"></div>' +
      '</div><div class="cat-count" id="cat-count"></div><div id="cat-results"></div>';
    var famSel = host.querySelector('#cat-fam'), boardSel = host.querySelector('#cat-board'), q = host.querySelector('#cat-q');
    var fams = uniq(EX.reduce(function (a, e) { e.boards.forEach(function (b) { a.push(b.family); }); return a; }, []));
    famSel.innerHTML = '<option value="">All families</option>' + fams.map(function (f) { return '<option>' + f + '</option>'; }).join('');

    function fillBoards() {
      var fam = famSel.value, cur = boardSel.value;
      var boards = uniq(EX.reduce(function (a, e) { e.boards.forEach(function (b) { if (!fam || b.family === fam) a.push(b.dir); }); return a; }, []));
      boardSel.innerHTML = '<option value="">All boards</option>' + boards.map(function (b) { return '<option>' + b + '</option>'; }).join('');
      if (boards.indexOf(cur) >= 0) boardSel.value = cur;
    }
    function render() {
      var fam = famSel.value, board = boardSel.value;
      var qs = q.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
      if (board) { try { localStorage.setItem(LS, board); } catch (e) {} }
      var list = EX.filter(function (e) {
        if (fam && !e.boards.some(function (b) { return b.family === fam; })) return false;
        if (board && !e.boards.some(function (b) { return b.dir === board; })) return false;
        if (qs.length) { var h = (e.name + ' ' + e.brief + ' ' + e.category + ' ' + e.path).toLowerCase(); if (!qs.every(function (t) { return h.indexOf(t) >= 0; })) return false; }
        return true;
      });
      host.querySelector('#cat-count').textContent = list.length + ' examples' + (board ? ' for ' + board : '') + (fam ? ' · ' + fam : '');
      var G = {};
      list.forEach(function (e) { var mm = meta(e.category); (G[mm[1]] = G[mm[1]] || {}); (G[mm[1]][mm[0]] = G[mm[1]][mm[0]] || []).push(e); });
      var groups = ORDER.filter(function (g) { return G[g]; }).concat(Object.keys(G).filter(function (g) { return ORDER.indexOf(g) < 0; }));
      host.querySelector('#cat-results').innerHTML = groups.map(function (g) {
        var total = Object.keys(G[g]).reduce(function (n, c) { return n + G[g][c].length; }, 0);
        var body = Object.keys(G[g]).sort().map(function (c) {
          var items = G[g][c].slice().sort(function (a, b) { var ra = pinRank(a.name), rb = pinRank(b.name); return ra !== rb ? ra - rb : a.name.localeCompare(b.name); });
          var cards = items.slice(0, 200).map(function (e) {
            var title = e.href ? ('<a href="' + e.href + '">' + e.name + '</a>') : ('<span class="nolink">' + e.name + '</span>');
            return '<div class="cat-card">' + title +
              '<div class="b ' + (e.brief ? '' : 'none') + '">' + (e.brief ? preview(e.brief) : '(no description)') + '</div></div>';
          }).join('');
          return '<div class="cat-sub">' + c + '<span class="n">' + G[g][c].length + '</span></div><div class="cat-grid">' + cards + '</div>';
        }).join('');
        return '<div class="cat-group"><span>' + g + '</span><span class="n">' + total + ' examples</span></div>' + body;
      }).join('');
    }
    fillBoards();
    var saved; try { saved = localStorage.getItem(LS); } catch (e) {}
    if (saved) boardSel.value = saved;
    famSel.addEventListener('change', function () { fillBoards(); render(); });
    boardSel.addEventListener('input', render);
    q.addEventListener('input', render);
    render();
  }
  if (document.readyState !== 'loading') init(); else document.addEventListener('DOMContentLoaded', init);
})();
"""


def setup(app: Sphinx) -> Dict[str, Any]:
    app.connect("builder-inited", build_catalog, priority=900)
    app.add_js_file(None, body=_CATALOG_JS)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
