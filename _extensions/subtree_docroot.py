"""
Subtree Docroot
###############

Copyright 2026 NXP
SPDX-License-Identifier: Apache-2.0

Introduction
============

Third-party documentation sets (e.g. Trusted Firmware-M) are authored as
standalone Sphinx projects: their doc-root-absolute references such as
``:doc:`/glossary``` or ``.. include:: /platform/foo.rst`` are written
against *their own* source root.  When such a tree is copied into the SDK
mono documentation tree (e.g. under ``middleware/tfm/tf-m/docs``), every
absolute reference misses by exactly that prefix.

This extension re-bases those references: absolute ``include``/
``literalinclude``/``image``/``figure`` directive paths are rewritten at
source-read time, while absolute ``:doc:`` role targets are resolved via
the ``missing-reference`` event (resolution-time handling avoids mutating
source text, which would break fixed-width RST grid tables).

It also registers a fallback ``uml`` directive (rendering the PlantUML
source as a literal block) when ``sphinxcontrib.plantuml`` is not loaded,
so upstream design documents build without the Java/PlantUML toolchain.

Configuration options
=====================

- ``subtree_docroots``: list of srcdir-relative directory prefixes (POSIX
  separators, no trailing slash) that hold standalone doc trees, e.g.
  ``middleware/tfm/tf-m/docs``.
"""

import re
from typing import Any, Dict

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

__version__ = "0.1.0"

#: sphinx directives that accept srcdir-absolute (/-prefixed) paths
_SPHINX_DIRECTIVE = re.compile(
    r"^(\s*\.\.\s+(?:literalinclude|image|figure)::\s+)/(?!/)",
    re.M,
)
#: docutils include: does NOT understand srcdir-absolute paths -> make relative
_INCLUDE_DIRECTIVE = re.compile(
    r"^(\s*\.\.\s+include::\s+)/(?!/)",
    re.M,
)


def rebase_subtree_files(app: Sphinx) -> None:
    """Rewrite absolute directive paths in the copied subtree files.

    File-level rewriting (rather than source-read) also covers content
    pulled in through ``.. include::`` chains, which bypasses the
    source-read event for the included file.
    """
    import pathlib

    srcdir = pathlib.Path(app.srcdir)
    for prefix in app.config.subtree_docroots:
        prefix = prefix.strip("/").rstrip("/")
        root = srcdir / prefix
        if not root.is_dir():
            continue
        for f in root.rglob("*.rst"):
            text = f.read_text(encoding="utf-8")
            new = _SPHINX_DIRECTIVE.sub(rf"\g<1>/{prefix}/", text)
            # docutils include anchors absolute paths at the filesystem
            # root, so re-base them relative to the including file
            depth = len(f.parent.relative_to(root).parts)
            updirs = "../" * depth if depth else "./"
            new = _INCLUDE_DIRECTIVE.sub(rf"\g<1>{updirs}", new)
            if new != text:
                f.write_text(new, encoding="utf-8")
                logger.info(f"subtree_docroot: re-based paths in {f.relative_to(srcdir)}")


def resolve_rebased_doc_ref(app: Sphinx, env, node, contnode):
    """Resolve :doc:`/absolute` references from subtree docs by re-basing."""
    if node.get("reftype") != "doc":
        return None
    target = str(node.get("reftarget", ""))
    refdoc = node.get("refdoc", "")
    if not target.startswith("/") or not refdoc:
        return None

    for prefix in app.config.subtree_docroots:
        prefix = prefix.strip("/").rstrip("/")
        if not refdoc.startswith(prefix + "/"):
            continue
        docname = prefix + target
        if docname not in env.all_docs:
            return None
        from sphinx.util.nodes import make_refnode
        if not node.get("refexplicit") and docname in env.titles:
            from sphinx.util.nodes import clean_astext
            caption = clean_astext(env.titles[docname])
            innernode = nodes.inline(caption, caption, classes=["doc"])
        else:
            innernode = contnode
        return make_refnode(app.builder, refdoc, docname, None, innernode)
    return None


class UmlFallbackDirective(Directive):
    """Render PlantUML sources as a literal block when plantuml is absent."""

    has_content = True
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec: Dict[str, Any] = {
        "caption": str,
        "scale": str,
        "align": str,
        "width": str,
        "height": str,
        "format": str,
    }

    def run(self):
        text = "\n".join(self.content)
        literal = nodes.literal_block(text, text)
        literal["language"] = "text"
        return [literal]


def register_uml_fallback(app: Sphinx) -> None:
    if "sphinxcontrib.plantuml" in app.config.extensions:
        return
    from docutils.parsers.rst import directives
    from docutils.parsers.rst.directives import _directives  # noqa: F401
    if "uml" not in directives._directives:
        app.add_directive("uml", UmlFallbackDirective)
        logger.info("subtree_docroot: registered uml fallback directive")


def register_section_labels(app: Sphinx, document) -> None:
    """Scoped equivalent of sphinx.ext.autosectionlabel.

    Upstream TF-M enables autosectionlabel with prefix_document=True, so its
    docs cross-reference sections as :ref:`docname:Section Title` (docname
    relative to *their* root).  Register those labels for subtree documents
    only, to avoid the duplicate-label storm a global autosectionlabel would
    cause in the SDK build.
    """
    env = app.env
    docname = env.docname
    for prefix in app.config.subtree_docroots:
        prefix = prefix.strip("/").rstrip("/")
        if not docname.startswith(prefix + "/"):
            continue
        reldoc = docname[len(prefix) + 1:]
        domain = env.get_domain("std")
        from sphinx.util.nodes import clean_astext
        for section in document.findall(nodes.section):
            if not section["ids"]:
                continue
            title = clean_astext(section[0])
            labelid = section["ids"][0]
            name = nodes.fully_normalize_name(f"{reldoc}:{title}")
            if name not in domain.labels:
                domain.anonlabels[name] = docname, labelid
                domain.labels[name] = docname, labelid, title
        return


def strip_leftover_pending_xrefs(app: Sphinx, doctree, docname: str) -> None:
    """Sanitize pending_xref nodes that escaped reference resolution.

    A pending_xref that survives into the writer raises NotImplementedError
    in the HTML translator and aborts the build.  For documents under the
    configured subtrees, resolve leftovers when the (re-based) target exists,
    otherwise degrade them to their inline content.
    """
    prefixes = [p.strip("/").rstrip("/") for p in app.config.subtree_docroots]
    if not any(docname.startswith(p + "/") for p in prefixes):
        return

    from sphinx.addnodes import pending_xref
    from sphinx.util.nodes import make_refnode

    for node in list(doctree.findall(pending_xref)):
        replacement = None
        target = str(node.get("reftarget", ""))
        if node.get("reftype") == "doc" and target.startswith("/"):
            for prefix in prefixes:
                if not docname.startswith(prefix + "/"):
                    continue
                todocname = prefix + target
                if todocname in app.env.all_docs:
                    child = node[0].deepcopy() if len(node) else nodes.inline(target, target)
                    replacement = make_refnode(
                        app.builder, docname, todocname, None, child
                    )
                break
        if replacement is None:
            logger.warning(
                f"subtree_docroot: unresolved reference {target!r} stripped",
                location=node,
            )
            replacement = node[0].deepcopy() if len(node) else nodes.inline(target, target)
        try:
            node.replace_self(replacement)
        except ValueError:
            # Detached node (shared between tree fragments) - the writer
            # fallback registered in setup() renders its children instead.
            pass


def _visit_pending_xref(self, node):  # render children as plain content
    pass


def _depart_pending_xref(self, node):
    pass


def setup(app: Sphinx) -> Dict[str, Any]:
    # Writer-level fallback: a pending_xref that escapes resolution (seen
    # with footnote references in upstream TF-M docs) must not crash the
    # HTML writer; render its inline content instead.
    from sphinx.addnodes import pending_xref
    app.add_node(
        pending_xref,
        override=True,
        html=(_visit_pending_xref, _depart_pending_xref),
        latex=(_visit_pending_xref, _depart_pending_xref),
        text=(_visit_pending_xref, _depart_pending_xref),
    )

    app.add_config_value("subtree_docroots", [], "env")
    # priority > external_content's sync so the copies exist before rewriting
    app.connect("builder-inited", rebase_subtree_files, priority=600)
    app.connect("doctree-read", register_section_labels)
    app.connect("missing-reference", resolve_rebased_doc_ref)
    app.connect("doctree-resolved", strip_leftover_pending_xrefs)
    app.connect("builder-inited", register_uml_fallback)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
