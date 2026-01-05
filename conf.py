# Unless otherwise indicated, all code in the Sphinx project is licenced under the two clause BSD licence below.
#
# Copyright (c) 2007-2024 by the Sphinx team (see AUTHORS file). All rights reserved.
# Copyright 2024-2025 NXP
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# Paths ------------------------------------------------------------------------

import os
import sys
from pathlib import Path
import re
import textwrap
import yaml
import json
from sphinx.cmd.build import get_parser
import sphinx_book_theme
from sphinx.util import logging

# -- MCUXpresso SDK Configuration Data ----------------------------------------
SDK_BASE = Path(__file__).absolute().parents[1]

logger = logging.getLogger("sphinx.config")

# Get build mode from environment variable
build_mode = os.environ.get('BUILD_MODE', 'original')
logger.info(f"Sphinx conf.py: Build mode = {build_mode}")

# Check if this is a PDF build
is_pdf_build = os.environ.get('SPHINX_TARGET', '').upper() in ['PDF', 'LATEX']
if is_pdf_build:
    logger.info("PDF/LaTeX build detected - all projects will use breathe mode")

# Patch the example_board_readme.md to avoid the warning
# WARNING: document isn't included in any toctree
def patch_example_readme_md(app, docname, source):
    if docname.endswith('example_board_readme') or docname.find('ChangeLog_') != -1 or docname.find('commonrn') != -1:
        source[0] = f'''---
orphan: true
---

{source[0]}
'''

def patch_mcuboot_readme(app, docname, source):
    """
    Patch the mcuboot README.md file for PDF builds.
    Replaces the license badge image with plain text.
    """
    # Only patch for PDF builds and if this is the mcuboot README
    if not is_pdf_build:
        return

    if 'middleware/mcuboot_opensource/README' in docname or docname.endswith('mcuboot_opensource/README'):
        logger.info(f"Patching mcuboot README for PDF build: {docname}")

        # Replace the license badge with plain text
        # Pattern: [![Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)][license]
        badge_pattern = r'\[!\[Apache 2\.0\]\(https://img\.shields\.io/badge/License-Apache%202\.0-blue\.svg\)\]\[license\]'
        replacement = 'License: Apache 2.0'

        # Also handle variations of the badge
        badge_pattern_alt = r'\[!\[.*?\]\(https://img\.shields\.io/badge/.*?\)\]\[.*?\]'

        original_content = source[0]

        # Try specific pattern first
        patched_content = re.sub(badge_pattern, replacement, original_content)

        # If no match, try alternative pattern
        if patched_content == original_content:
            patched_content = re.sub(badge_pattern_alt, replacement, original_content)

        if patched_content != original_content:
            source[0] = patched_content
            logger.info(f"Successfully patched license badge in {docname}")
        else:
            logger.warning(f"License badge pattern not found in {docname}")

def setup(app):
    app.connect('source-read', patch_example_readme_md)
    app.connect('source-read', patch_mcuboot_readme)

# Parse command line arguments
args = get_parser().parse_args()

# Extract the -D parameters
d_params = {}
if args.define:
    for item in args.define:
        key, value = item.split('=', 1)
        d_params[key] = value

logger.debug(f"Command line parameters: {d_params}")

# Get board target if specified
board_target = d_params.get('board_target', None)

# Collect tags
example_scope = d_params.get('example_scope', '')
for tag in d_params.get('tags', '').split(','):
    if tag and not tags.has(tag):  # pylint: disable=undefined-variable
        tags.add(tag)  # pylint: disable=undefined-variable
        logger.debug(f"Adding tag: {tag}")

# Initialize ConfigurationManager
DOC_BASE = SDK_BASE / "docs"
sys.path.insert(0, str(DOC_BASE))
sys.path.insert(0, str(DOC_BASE / "_extensions"))

from config_manager import ConfigurationManager

mcux_config = ConfigurationManager(
    sdk_base=SDK_BASE,
    user_tags=tags,  # pylint: disable=undefined-variable
    example_scope=example_scope,
    build_mode=build_mode,
    board_target=board_target
)

DOC_BUILD = Path(args.outputdir).resolve().parents[0]

# -- Project information -----------------------------------------------------

project = mcux_config.project
copyright = mcux_config.copyright
author = mcux_config.author
release = mcux_config.version
version = release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = mcux_config.get_extensions()
source_suffix = mcux_config.get_source_suffix()

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    "papersize": "a4paper",
    "maketitle": open(SDK_BASE / "docs" / "_static" / "latex" / "title.tex").read(),
    "preamble": open(SDK_BASE / "docs" / "_static" / "latex" / "preamble.tex").read(),
    "makeindex": r"\usepackage[columns=1]{idxlayout}\makeindex",
    "fontpkg": textwrap.dedent(r"""
                                    \usepackage{noto}
                                    \usepackage{inconsolata}
                                    \usepackage[T1]{fontenc}
                                """),
    "sphinxsetup": ",".join(
        (
            # NOTE: colors match those found in light.css stylesheet
            "verbatimwithframe=false",
            "VerbatimColor={HTML}{f0f2f4}",
            "InnerLinkColor={HTML}{2980b9}",
            "warningBgColor={HTML}{e9a499}",
            "warningborder=0pt",
            r"HeaderFamily=\rmfamily\bfseries",
        )
    ),
}
latex_logo = str(SDK_BASE / "docs" / "internal" / "images" / "logo-nxp.pdf")

# Set master document
master_doc = mcux_config.get_master_doc()

# Create board index if needed
if board_target:
    mcux_config.create_board_index(DOC_BASE)

if board_target:
    latex_documents = [
        (master_doc, f"mcuxsdk-{board_target}.tex", "MCUXpresso SDK Documentation", author, "manual"),
    ]
else:
    latex_documents = [
        ("index-tex", "mcuxsdk.tex", "MCUXpresso SDK Documentation", author, "manual"),
    ]

latex_engine = "xelatex"

# -- Options for doxyrunner plugins ---------------------------------

# Get doxygen projects organized by extension
if mcux_config.has_doxygen_projects:
    doxygen_projects = mcux_config.get_doxygen_projects_by_extension(DOC_BUILD)

    # Configure doxyrunner (breathe mode)
    if doxygen_projects['doxyrunner'] and 'doxyrunner' in extensions:
        doxyrunner_doxygen = os.environ.get("DOXYGEN_EXECUTABLE", "doxygen")
        doxyrunner_doxydicts = {
            proj['name']: {
                'doxyfile': proj['doxyfile'],
                'outdir': proj['outdir']
            }
            for proj in doxygen_projects['doxyrunner']
        }
        doxyrunner_fmt = True
        doxyrunner_fmt_vars = {"SDK_BASE": str(SDK_BASE)}
        doxyrunner_outdir_var = "DOXY_OUT"

        logger.info(f"Configured {len(doxyrunner_doxydicts)} projects for doxyrunner (breathe)")

    # Configure breathe
    if 'breathe' in extensions:
        breathe_projects = mcux_config.get_breathe_projects(DOC_BUILD)
        breathe_default_project = list(breathe_projects.keys())[0] if breathe_projects else ""
        breathe_separate_member_pages = True
        breathe_domain_by_extension = {
            "h": "c",
            "c": "c",
        }

        logger.info(f"Configured {len(breathe_projects)} projects for breathe")

    # Configure doxyrunner_html
    if doxygen_projects['doxyrunner_html'] and 'doxyrunner_html' in extensions:
        doxyrunner_html_doxygen = os.environ.get("DOXYGEN_EXECUTABLE", "doxygen")
        doxyrunner_html_doxydicts = {
            proj['name']: {
                'doxyfile': proj['doxyfile'],
                'outdir': proj['outdir']
            }
            for proj in doxygen_projects['doxyrunner_html']
        }
        doxyrunner_html_fmt = True
        doxyrunner_html_fmt_vars = {"SDK_BASE": str(SDK_BASE)}
        doxyrunner_html_outdir_var = "DOXY_OUT"
        doxyrunner_html_mode = 1

        logger.info(f"Configured {len(doxyrunner_html_doxydicts)} projects for doxyrunner_html")

    # Configure doxyrunner_sphinx
    if doxygen_projects['doxyrunner_sphinx'] and 'doxyrunner_sphinx' in extensions:
        doxyrunner_sphinx_doxygen = os.environ.get("DOXYGEN_EXECUTABLE", "doxygen")
        doxyrunner_sphinx_doxydicts = {
            proj['name']: {
                'doxyfile': proj['doxyfile'],
                'outdir': proj['outdir']
            }
            for proj in doxygen_projects['doxyrunner_sphinx']
        }
        doxyrunner_sphinx_fmt = True
        doxyrunner_sphinx_fmt_vars = {"SDK_BASE": str(SDK_BASE)}
        doxyrunner_sphinx_outdir_var = "DOXY_OUT"
        doxyrunner_sphinx_mode = 1

        logger.info(f"Configured {len(doxyrunner_sphinx_doxydicts)} projects for doxyrunner_sphinx")

# Set up inline comments
comments_config = {
   "dokieli": True
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_book_theme'


# Updated theme options for sphinx_book_theme
html_theme_options = {
    "repository_url": "https://github.com/nxp-mcuxpresso/mcuxsdk-doc",  # Update with your actual repo
    "use_repository_button": False,
    "use_issues_button": False,
    "use_edit_page_button": False,
    "use_download_button": False,
    "show_toc_level": 2,
    "collapse_navigation": True,
    "navigation_with_keys": True,
    "show_navbar_depth": 1,
    "navigation_depth": 3,
    "use_sidenotes": True,
    "announcement": None,  # Can be used for announcements
    "home_page_in_toc": True,
    "use_fullscreen_button": False,
}

# Keep your existing configuration
html_baseurl = "https://kex-dev.nxp.com/docs/latest/"
html_title = "MCUXpresso SDK Documentation"

# Update static paths - sphinx_book_theme has different requirements
static_path = [str(DOC_BASE / "_static")]
if os.path.exists(os.path.join(DOC_BASE, "internal")):
    static_path.append(str(DOC_BASE / "internal" / "public"))
    static_path.append(str(DOC_BASE / "internal" / "images"))
    html_logo = str(DOC_BASE / "internal" / "images" / "nxp_logo_small.png")
    html_favicon = str(DOC_BASE / "internal" / "images" / "nxp_logo_small.png")

html_static_path = static_path
html_last_updated_fmt = "%b %d, %Y %H:%M%z"
html_domain_indices = False
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False

# Get existing variables
docgen_branch = os.getenv("DOCGEN_BRANCH")
docgen_rev = os.getenv("DOCGEN_REV")

# Add CSS files for customization
html_css_files = [
    'book_theme_custom.css',  # New CSS file for book theme customizations
]

is_release = tags.has("release")  # pylint: disable=undefined-variable
reference_prefix = DOC_BUILD
if tags.has("publish"):  # pylint: disable=undefined-variable
    reference_prefix = f"/{version}" if is_release else "/latest"
docs_title = "Docs"

# Define html_context (this was missing in the original)
html_context = {
    "show_license": True,
    "docs_title": docs_title,
    "is_release": is_release,
    "current_version": version,
    "branch_info": docgen_branch,
    "rev_info": docgen_rev,
    "display_vcs_link": True,
    "html_title": html_title
}

# Keep your existing version handling
is_internal_doc = mcux_config.is_internal_doc
with open(DOC_BASE / "versions.json", "r", encoding="utf-8") as f:
    versions_data = json.load(f)
if is_internal_doc:
    version_list = [(version, f"/mcuxsdk-internal/{('release-' + version) if version != "latest" else version}/html/") for version in versions_data]
else:
    version_list = [(version, f"/mcuxsdk/{version}/html/") for version in versions_data]

html_context["versions"] = tuple(version_list)


# -- Options for notfound.extension ---------------------------------------
if is_internal_doc:
    notfound_urls_prefix = f"/mcuxsdk-internal/release-{version}/html/" if is_release else "/mcuxsdk-internal/main/html/"
else:
    notfound_urls_prefix =  f"/mcuxsdk/{version}/html/" if is_release else "/mcuxsdk/latest/html/"

# -- Options for vcs_link ------------------------------------------
if 'vcs_link' in extensions:
    vcs_link_prefixes = mcux_config.get_vcs_links()
    vcs_link_version = f"release/{version}" if is_release else "main"

# -- Options for external_content ----------------------------------
if 'external_content' in extensions:
    external_content_contents = mcux_config.get_external_contents()
    external_content_keep = []

suppress_warnings = [
    "myst.header", # WARNING: Non-consecutive header level increase; H4 to H7 [myst.header]
    'image.fetch'
]
# suppress_warnings = ['image.fetch']
# conf.py
image_fetch_timeout = 1  # Timeout in seconds
myst_heading_anchors = 6
#myst_all_links_external = False

# Build mode specific final configuration
logger.info(f"=== Sphinx Configuration Summary ===")
logger.info(f"Driver Build Mode: {build_mode}")
if is_pdf_build:
    logger.info(f"PDF/LaTeX Build: Yes (all projects use breathe)")
logger.info(f"Project: {project}")
logger.info(f"Extensions: {len(extensions)} loaded")
logger.info(f"  - {', '.join(extensions)}")

if mcux_config.has_doxygen_projects:
    logger.info(f"Doxygen Projects Configuration:")

    if 'doxyrunner_doxydicts' in locals():
        logger.info(f"  - doxyrunner (breathe): {len(doxyrunner_doxydicts)} projects")
        for name in doxyrunner_doxydicts.keys():
            logger.info(f"    * {name}")

    if 'doxyrunner_html_doxydicts' in locals():
        logger.info(f"  - doxyrunner_html: {len(doxyrunner_html_doxydicts)} projects")
        for name in doxyrunner_html_doxydicts.keys():
            logger.info(f"    * {name}")

    if 'doxyrunner_sphinx_doxydicts' in locals():
        logger.info(f"  - doxyrunner_sphinx: {len(doxyrunner_sphinx_doxydicts)} projects")
        for name in doxyrunner_sphinx_doxydicts.keys():
            logger.info(f"    * {name}")

    if 'breathe_projects' in locals():
        logger.info(f"  - breathe projects: {len(breathe_projects)}")

logger.info(f"HTML Title: {html_title}")
logger.info(f"Master Document: {master_doc}")
logger.info(f"=====================================")
