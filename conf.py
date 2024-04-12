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
from pathlib import Path
import re
import textwrap
import sys,subprocess
from sphinx.cmd.build import get_parser

args = get_parser().parse_args()

DOC_BASE = Path(__file__).absolute().parents[0]
SDK_BASE = Path(__file__).absolute().parents[1]
print(SDK_BASE)
DOC_BUILD = Path(args.outputdir).resolve().parents[0]
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, DOC_BASE)
sys.path.insert(0, str(DOC_BASE / "_extensions"))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'mcuxsdk'
copyright = '2021,2024, NXP'
author = 'NXP'

# parse version from 'VERSION' file
with open(SDK_BASE / "VERSION") as f:
    m = re.match(
        (
            r"^CURRENT_YEAR\s*=\s*(\d+)$\n"
            + r"^VERSION_MAJOR\s*=\s*(\d+)$\n"
            + r"^VERSION_MINOR\s*=\s*(\d+)$\n"
            + r"^PATCHLEVEL\s*=\s*(\d+)$\n"
            + r"^EXTRAVERSION\s*=\s*(.*)$"
        ),
        f.read(),
        re.MULTILINE,
    )

    if not m:
        sys.stderr.write("Warning: Could not extract SDK version\n")
        version = "Unknown"
    else:
        year, major, minor, patch, extra = m.groups(1)
        version = ".".join((year, major, minor, patch))
        if extra:
            version += "-" + extra


# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
"sphinx_rtd_theme",
# 'sphinx.ext.autodoc',
"sphinx.ext.extlinks",
"vcs_link",
'sphinx.ext.todo',
'sphinx.ext.extlinks',
'sphinx.ext.autodoc',
"myst_parser",
"breathe",
"doxyrunner",
"external_content"
#"warnings_filter"
# 'exhale'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.readme': 'markdown',
    '.md': 'markdown',
}

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    "papersize": "a4paper",
    "maketitle": open(SDK_BASE / "docs" / "_static" / "latex" / "title.tex").read(),
    "preamble": open(SDK_BASE / "docs" / "_static" / "latex" / "preamble.tex").read(),
    "makeindex": r"\usepackage[columns=1]{idxlayout}\makeindex",
    "fontpkg": textwrap.dedent(r"""
                                    \usepackage{noto}
                                    \usepackage{inconsolata-nerd-font}
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
latex_logo = str(SDK_BASE / "docs" / "_static" / "images" / "logo-nxp.pdf")
latex_documents = [
    ("index", "mcuxsdk.tex", "MCUXpresso SDK Documentation", author, "manual"),
]
latex_engine = "xelatex"

# -- Options for doxyrunner plugin ---------------------------------

doxyrunner_doxygen = os.environ.get("DOXYGEN_EXECUTABLE", "doxygen")
doxyrunner_doxyfile = DOC_BASE / "Doxyfile_lib_PDF_RM_Drivers"
doxyrunner_outdir = DOC_BUILD / "doxygen"
doxyrunner_fmt = True
doxyrunner_fmt_vars = {"SDK_BASE": str(SDK_BASE)}
doxyrunner_outdir_var = "DOXY_OUT"

print(f"doxygen runner configuration: {doxyrunner_outdir}")
# Breathe Configuration
breathe_projects = {"Drivers": str(doxyrunner_outdir / "xml")}
breathe_default_project = "Drivers"
breathe_separate_member_pages = True

# # Setup the exhale extension
# exhale_args = {
    # # These arguments are required
    # "containmentFolder":     "./reference",
    # "rootFileName":          "reference.rst",
    # "rootFileTitle":         "Reference API",
    # "doxygenStripFromPath":  "..",
    # # Suggested optional arguments
    # "createTreeView":        True,
    # # TIP: if using the sphinx-bootstrap-theme, you need
    # # "treeViewIsBootstrap": True,
    # "exhaleExecutesDoxygen": True,
    # "exhaleDoxygenStdin":    "INPUT = ../drivers/acmp/ \
                                      # ../drivers/crc/ "
# }

# # Tell sphinx what the primary language being documented is.
# primary_domain = 'c'

# # Tell sphinx what the pygments highlight language should be.
# highlight_language = 'c'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
# html_extra_path = ['../SW-Content-Register.txt', '../COPYING-BSD-3', '../CMSIS/LICENSE.txt']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "logo_only": True,
    "prev_next_buttons_location": None
}
html_baseurl = "https://docs.zephyrproject.org/latest/"
html_title = "MCUXpresso SDK Documentation"
html_logo = str(DOC_BASE / "_static" / "images" / "fs_logo.gif")
html_favicon = str(DOC_BASE / "_static" / "images" / "nxp_logo_small.png")
html_static_path = [str(DOC_BASE / "_static")]
html_last_updated_fmt = "%b %d, %Y"
html_domain_indices = False
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False

is_release = tags.has("release")  # pylint: disable=undefined-variable
reference_prefix = DOC_BUILD
if tags.has("publish"):  # pylint: disable=undefined-variable
    reference_prefix = f"/{version}" if is_release else "/latest"
docs_title = "Docs / {}".format(version if is_release else "Latest")
html_context = {
    "show_license": True,
    "docs_title": docs_title,
    "is_release": is_release,
    "current_version": version,
    "versions": (
        ("latest", "/"),
        ("24.3.0.0", "/24.3.0.0/"),
        ("24.3.1.0", "/24.3.1.0/"),
    ),
    "display_vcs_link": True,
    "reference_links": {
        "API Reference Manual": f"{reference_prefix}/doxygen/html/index.html",
    },
}
# -- Options for vcs_link ------------------------------------------
vcs_link_prefixes = {
    "examples/.*readme": "https://bitbucket.sw.nxp.com/projects/SCM/repos/mcu-sdk-examples/browse",
    "boards/.*readme": "https://bitbucket.sw.nxp.com/projects/SCM/repos/mcu-sdk-boards/browse",
    "Boards/.*readme": "https://bitbucket.sw.nxp.com/projects/SCM/repos/mcu-sdk-boards/browse",
    ".*": "https://bitbucket.sw.nxp.com/projects/SCM/repos/mcu-sdk-doc/browse",
}

#vcs_link_base_url = "https://bitbucket.sw.nxp.com/projects/SCM/repos/mcu-sdk-doc/browse"

# -- Options for zephyr.external_content ----------------------------------

external_content_contents = [
    (SDK_BASE / "docs", "[!_]*"),
    (SDK_BASE, "examples/index.rst"),
    (SDK_BASE, "examples/*/index.rst"),
    (SDK_BASE, "examples/*/**/index.rst"),
    (SDK_BASE, "examples/**/**/*.readme"),
    (SDK_BASE, "examples/**/**/**/*.readme"),
    (SDK_BASE, "boards/**/**/*.readme"),
    (SDK_BASE, "boards/**/**/**/*.readme"),
]
external_content_keep = [
]