"""
Source Pages
############

Copyright 2026 NXP
SPDX-License-Identifier: Apache-2.0

Introduction
============

Documentation pages frequently reference source files that ship with the SDK
(configuration headers, linker scripts, CMake/Kconfig fragments).  Sphinx only
builds pages from md/rst sources, so markdown links to such files can never
resolve and are reported as broken references.

This extension generates a syntax-highlighted viewer page for every source
file listed in the ``source_pages_files`` configuration value:

- the raw file is copied from the workspace into ``_sources_view/`` inside the
  Sphinx source tree,
- a wrapper page embedding it via ``literalinclude`` (with the appropriate
  Pygments lexer and line numbers) is generated next to it,
- a minimal Sphinx domain resolves MyST links whose target matches a
  registered source file to the generated viewer page (myst-parser consults
  every domain's ``resolve_any_xref`` for ``[text](target)`` links), so
  authors can keep writing natural relative links such as
  ``[nxp_iot_agent_config.h](../inc/nxp_iot_agent_config.h)``.

Configuration options
=====================

- ``source_pages_files``: list of workspace-relative paths (POSIX separators)
  of source files to expose, e.g.
  ``middleware/nxp_iot_agent/inc/nxp_iot_agent_config.h``.
"""

import os
import shutil
from pathlib import Path
from typing import Any, Dict, List, Tuple

from docutils.nodes import Element
from sphinx.application import Sphinx
from sphinx.domains import Domain
from sphinx.util import logging
from sphinx.util.nodes import make_refnode

logger = logging.getLogger(__name__)

__version__ = "0.1.0"

VIEW_DIR = "_sources_view"

#: file name / suffix -> Pygments lexer
_LEXERS = {
    ".c": "c",
    ".h": "c",
    ".cpp": "cpp",
    ".hpp": "cpp",
    ".py": "python",
    ".json": "json",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".cmake": "cmake",
    "CMakeLists.txt": "cmake",
    "Kconfig": "kconfig",
    ".dts": "dts",
    ".dtsi": "dts",
    ".ld": "text",
    ".icf": "text",
    ".scf": "text",
    ".txt": "text",
}


def _lexer_for(path: str) -> str:
    name = os.path.basename(path)
    if name in _LEXERS:
        return _LEXERS[name]
    return _LEXERS.get(Path(name).suffix.lower(), "text")


def _sdk_base(app: Sphinx) -> Path:
    # docs/ lives directly under the SDK root; conf.py sits in docs/.
    return Path(app.confdir).parents[0]


def generate_pages(app: Sphinx) -> None:
    """Copy raw sources and generate viewer pages (builder-inited)."""
    files = app.config.source_pages_files
    if not files:
        return

    sdk_base = _sdk_base(app)
    srcdir = Path(app.srcdir)
    registry: Dict[str, str] = {}

    for rel in files:
        rel = rel.strip().replace("\\", "/").lstrip("/")
        src = sdk_base / rel
        if not src.is_file():
            logger.warning(f"source_pages: file not found, skipped: {rel}")
            continue

        raw_dst = srcdir / VIEW_DIR / rel
        raw_dst.parent.mkdir(parents=True, exist_ok=True)
        if not raw_dst.exists() or src.stat().st_mtime > raw_dst.stat().st_mtime:
            shutil.copyfile(src, raw_dst)

        title = f"``{rel}``"
        content = (
            f":orphan:\n\n"
            f"{title}\n"
            f"{'#' * len(title)}\n\n"
            f".. literalinclude:: {raw_dst.name}\n"
            f"   :language: {_lexer_for(rel)}\n"
            f"   :linenos:\n"
        )
        page = raw_dst.with_name(raw_dst.name + ".rst")
        if not page.exists() or page.read_text(encoding="utf-8") != content:
            page.write_text(content, encoding="utf-8")

        # Sphinx docname of the generated page (suffix stripped)
        registry[rel] = f"{VIEW_DIR}/{rel}"

    app.env.source_pages_registry = registry  # type: ignore[attr-defined]
    logger.info(f"source_pages: generated {len(registry)} viewer page(s)")


class SourceFilesDomain(Domain):
    """Resolves links whose target is a registered source file.

    myst-parser resolves ``[text](target)`` links by consulting every
    domain's ``resolve_any_xref``, which makes a domain the reliable hook
    point (myst does not dispatch Sphinx's ``missing-reference`` event).
    """

    name = "srcfile"
    label = "Source files"

    def resolve_any_xref(
        self, env, fromdocname: str, builder, target: str, node, contnode: Element
    ) -> List[Tuple[str, Element]]:
        registry = getattr(env, "source_pages_registry", None)
        if not registry:
            return []

        target = str(target).split("#")[0].replace("\\", "/")
        if not target or target.endswith((".md", ".rst")):
            return []

        if target.startswith("/"):
            resolved = target.lstrip("/")
        else:
            base = os.path.dirname(str(env.doc2path(fromdocname, False)))
            resolved = os.path.normpath(os.path.join(base, target)).replace("\\", "/")

        for rel, docname in registry.items():
            if resolved == rel or resolved.endswith("/" + rel):
                ref = make_refnode(builder, fromdocname, docname, None, contnode, rel)
                return [("srcfile:file", ref)]
        return []

    def merge_domaindata(self, docnames, otherdata) -> None:
        pass


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("source_pages_files", [], "env")
    app.add_domain(SourceFilesDomain)
    app.connect("builder-inited", generate_pages)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
