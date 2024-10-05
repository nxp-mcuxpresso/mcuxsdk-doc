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
import copy
from pathlib import Path
import yaml
import re
import textwrap
import sys,subprocess
from sphinx.cmd.build import get_parser

# -- MCUXpresso SDK Configuration Data ----------------------------------------
SDK_BASE = Path(__file__).absolute().parents[1]

class MCUXDocConfig:
    '''MCUXpresso SDK Configuration Data Class to simplify the feeding of configuration data'''
    NAME = 'default'
    def __init__(self, user_tags):
        # Read the user config
        with open(SDK_BASE / 'docs' / '_cfg' / 'user_config.yml', 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        # Find matched tags
        self.user_tags = user_tags
        print('-- MCUXDocConfig Tags')
        for tag in self.user_tags:
            print(f'  [+] {tag}')

        # Match with module tag
        self.module_tags = []
        for module_name in self.config['modules']:
            if any([re.fullmatch(tag, module_name) for tag in self.user_tags]):
                self.module_tags.append(module_name)
        if not self.module_tags:
            for module_name, module_config in self.config['modules'].items():
                if module_config.get('default', False):
                    self.module_tags.append(module_name)

        print('-- MCUXDocConfig User Modules')
        for module in self.module_tags:
            print(f'  [+] {module}')

    @property
    def project(self):
        return self.config.get('project', 'mcuxsdk')

    @property
    def copyright(self):
        return self.config.get('copyright', '2021,2024, NXP')

    @property
    def author(self):
        return self.config.get('author', 'NXP')

    @property
    def version(self):
        with open(SDK_BASE / "MCUX_VERSION") as f:
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
                matched_version = "Unknown"
            else:
                year, major, minor, patch, extra = m.groups(1)
                matched_version= ".".join((year, major, minor, patch))
                if extra:
                    matched_version += "-" + extra

        return matched_version

    def iter_modules(self):
        for module_name in self.module_tags:
            module_config = self.config['modules'][module_name]
            yield module_name, module_config

    @property
    def extensions(self):
        print('-- Collect Extensions')
        my_extensions = self.config['extensions']

        for module_name, module_config in self.iter_modules():
            if not module_config.get('extensions', []):
                continue
            print(f'  [+] extensions from {module_name}')
            my_extensions.extend(module_config['extensions'])

        return my_extensions

    @property
    def source_suffix(self):
        return self.config['source_suffix']

    @property
    def external_content_contents(self):
        print('-- Collect External Content')
        contents = [
            (SDK_BASE / item['root'], item['pattern']) for item in self.config.get('external_contents', [])
        ]
        for module_name, module_config in self.iter_modules():
            if not module_config.get('external_contents', []):
                continue
            print(f'  [+] external content from {module_name}')
            contents.extend(
                [
                    (SDK_BASE/item['root'], item['pattern']) for item in module_config['external_contents']
                ]
            )

        return contents

    @property
    def external_content_keep(self):
        return []

    @property
    def vcs_link(self):
        print('-- Collect VCS Link')
        links = {}

        for module_name, module_config in self.iter_modules():
            if not module_config.get('vcs_link', {}):
                continue
            print(f'  [+] vcs link from {module_name}')
            links.update({
                item["pattern"]: item["link"] for item in module_config['vcs_link']
            })

        links.update({
            item["pattern"]: item["link"] for item in self.config.get('vcs_link', [])
        })

        return links

mcux_config = MCUXDocConfig(tags)

# -- Functions -----------------------------------------------------------------
# def search_sdk_base():
#     # starting from current path, if its parent path
#     # get file Kconfig.mcuxpresso in the folder, then the path is the SDK base
#     current_path = Path(__file__).absolute()
#     for _ in range(5):
#         if (current_path / "Kconfig.mcuxpresso").exists():
#             print(f"-- Found SDK base path: {current_path}")
#             return current_path
#         current_path = current_path.parent
#     raise RuntimeError(f"-- Cannot find SDK base path starting from {Path(__file__).absolute()}")

args = get_parser().parse_args()
# SDK_BASE = search_sdk_base()
DOC_BASE = SDK_BASE / "docs"
DOC_BUILD = Path(args.outputdir).resolve().parents[0]
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, DOC_BASE)
sys.path.insert(0, str(DOC_BASE / "_extensions"))
import sphinx_rtd_theme

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
extensions = mcux_config.extensions
source_suffix = mcux_config.source_suffix

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

if 'doxyrunner' in extensions:
    doxyrunner_doxygen = os.environ.get("DOXYGEN_EXECUTABLE", "doxygen")
    doxyrunner_doxyfile = DOC_BASE / "drivers" / "Doxyfile_lib_PDF_RM_Drivers"
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
templates_path = ['../../_templates']

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
    'navigation_depth': 5,
    "prev_next_buttons_location": None
}
html_baseurl = "https://docs.zephyrproject.org/latest/"
html_title = "MCUXpresso SDK Documentation"
html_logo = str(DOC_BASE / "_static" / "images" / "nxp_logo_small.png")
html_favicon = str(DOC_BASE / "_static" / "images" / "nxp_logo_small.png")
html_static_path = [str(DOC_BASE / "_static")]
html_last_updated_fmt = "%b %d, %Y"
html_domain_indices = False
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
docgen_branch = os.getenv("DOCGEN_BRANCH")
docgen_rev = os.getenv("DOCGEN_REV")

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
    "branch_info": docgen_branch,
    "rev_info": docgen_rev,
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
if 'vcs_link' in extensions:
    vcs_link_prefixes = mcux_config.vcs_link

#vcs_link_base_url = "https://bitbucket.sw.nxp.com/projects/SCM/repos/mcu-sdk-doc/browse"

# -- Options for zephyr.external_content ----------------------------------
if 'external_content' in extensions:
    external_content_contents = mcux_config.external_content_contents
    external_content_keep = mcux_config.external_content_keep
