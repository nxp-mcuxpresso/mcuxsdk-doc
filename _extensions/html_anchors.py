"""
HTML Anchors
############

Copyright 2026 NXP
SPDX-License-Identifier: Apache-2.0

Introduction
============

Documentation converted from Doxygen or DITA frequently anchors table rows
and inline spans with raw HTML (``<a name="x"></a>`` / ``<a id="x"></a>``),
because Markdown has no way to attach a target inside a table cell.  MyST
passes the raw HTML through to the rendered page - the anchor works in the
browser - but does not register it as a cross-reference target, so every
``[text](#x)`` link referencing it fails with ``xref_target_not_found``.

This extension makes such anchors first-class targets without touching the
(often auto-generated) source files:

- at ``doctree-read`` it scans documents under the configured prefixes for
  raw-HTML anchor definitions and records ``anchor -> docname``,
- a minimal Sphinx domain resolves MyST links whose target matches a
  recorded anchor to ``page.html#anchor`` (myst-parser consults every
  domain's ``resolve_any_xref`` for ``[text](target)`` links).

Configuration options
=====================

- ``html_anchor_docroots``: list of docname prefixes (POSIX separators) to
  scan for raw HTML anchors, e.g. ``middleware/eiq/mpp/docs``.
"""

import re
from typing import Any, Dict, List, Tuple

from docutils import nodes
from docutils.nodes import Element
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.domains import Domain
from sphinx.errors import NoUri
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging
from sphinx.util.nodes import make_refnode

logger = logging.getLogger(__name__)

__version__ = "0.1.0"

_ANCHOR = re.compile(r'<a\s+(?:name|id)="([^"]+)"\s*>')


def _in_scope(app: Sphinx, docname: str) -> bool:
    for prefix in app.config.html_anchor_docroots:
        prefix = prefix.strip("/").rstrip("/")
        if docname == prefix or docname.startswith(prefix + "/"):
            return True
    return False


def collect_anchors(app: Sphinx, doctree) -> None:
    env = app.env
    docname = env.docname
    if not _in_scope(app, docname):
        return
    registry = getattr(env, "html_anchor_map", None)
    if registry is None:
        registry = env.html_anchor_map = {}
    found = 0
    for node in doctree.findall(nodes.raw):
        if node.get("format") != "html":
            continue
        for m in _ANCHOR.finditer(node.astext()):
            docs = registry.setdefault(m.group(1), [])
            if docname not in docs:
                docs.append(docname)
            found += 1
    if found:
        logger.debug(f"html_anchors: {found} anchor(s) in {docname}")


def _lookup(registry, anchor: str, prefer_doc: str = None):
    """Return (docname, anchor-as-recorded) preferring the referring doc.

    The same anchor may legitimately exist in several documents (e.g.
    per-board copies of a converted topic); a reference prefers the anchor
    in its own document, falling back to the first recorded one.
    """
    for key in (anchor, anchor.lower()):
        docs = registry.get(key)
        if docs:
            if prefer_doc and prefer_doc in docs:
                return prefer_doc, key
            return docs[0], key
    return None, None


def purge_doc(app: Sphinx, env, docname: str) -> None:
    registry = getattr(env, "html_anchor_map", None)
    if registry:
        for k in list(registry):
            registry[k] = [d for d in registry[k] if d != docname]
            if not registry[k]:
                del registry[k]


def merge_info(app: Sphinx, env, docnames, other) -> None:
    registry = getattr(env, "html_anchor_map", None)
    other_reg = getattr(other, "html_anchor_map", None)
    if other_reg:
        if registry is None:
            registry = env.html_anchor_map = {}
        for k, docs in other_reg.items():
            dst = registry.setdefault(k, [])
            for d in docs:
                if d not in dst:
                    dst.append(d)


class HtmlAnchorDomain(Domain):
    """Resolves links whose target matches a recorded raw-HTML anchor."""

    name = "htmlanchor"
    label = "Raw HTML anchors"

    def resolve_any_xref(
        self, env, fromdocname: str, builder, target: str, node, contnode: Element
    ) -> List[Tuple[str, Element]]:
        registry = getattr(env, "html_anchor_map", None)
        if not registry:
            return []
        anchor = str(target).lstrip("#")
        docname, key = _lookup(registry, anchor, prefer_doc=fromdocname)
        if not docname:
            return []
        try:
            refuri = builder.get_relative_uri(fromdocname, docname) + "#" + key
        except Exception:  # pylint: disable=broad-except
            return []
        ref = nodes.reference("", "", internal=True, refuri=refuri)
        ref.append(contnode)
        return [("htmlanchor:anchor", ref)]

    def merge_domaindata(self, docnames, otherdata) -> None:
        pass


class DocFragmentResolver(SphinxPostTransform):
    """Resolve ``[text](file.md#X)`` links against labels and raw anchors.

    myst-parser resolves the doc-plus-fragment link form against heading
    slugs only (``env.metadata[doc]['myst_slugs']``); ``(X)=`` labels and
    raw HTML anchors are invisible to it, producing ``local id not found``
    warnings even though the target exists on the rendered page.  This
    post-transform runs just before MystReferenceResolver (priority 9) and
    resolves the fragment case-insensitively against:

    - std-domain labels defined in the target document (``(X)=`` targets),
    - raw HTML anchors recorded by this extension.
    """

    default_priority = 8

    def run(self, **kwargs: Any) -> None:
        env = self.env
        for node in list(self.document.findall(addnodes.pending_xref)):
            if node.get("reftype") != "myst" or node.get("refdomain") != "doc":
                continue
            ref_id = node.get("reftargetid")
            docname = node.get("reftarget")
            if not ref_id or not docname or docname not in env.all_docs:
                continue
            # heading slugs are myst's own business - leave those to it
            if ref_id in env.metadata.get(docname, {}).get("myst_slugs", {}):
                continue

            targetid = None
            low = ref_id.lower()
            std = env.get_domain("std")
            for registry in (std.labels, std.anonlabels):
                entry = registry.get(low)
                if entry and entry[0] == docname:
                    targetid = entry[1]
                    break
            if targetid is None:
                anchors = getattr(env, "html_anchor_map", None) or {}
                for key in (ref_id, low):
                    if docname in (anchors.get(key) or []):
                        targetid = key
                        break
            if targetid is None:
                continue

            contnode = node[0].deepcopy()
            try:
                ref = make_refnode(
                    self.app.builder, env.docname, docname, targetid, contnode
                )
            except NoUri:
                ref = contnode
            node.replace_self(ref)


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("html_anchor_docroots", [], "env")
    app.add_domain(HtmlAnchorDomain)
    app.add_post_transform(DocFragmentResolver)
    app.connect("doctree-read", collect_anchors)
    app.connect("env-purge-doc", purge_doc)
    app.connect("env-merge-info", merge_info)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
