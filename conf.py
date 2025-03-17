# Unless otherwise indicated, all code in the Sphinx project is licenced under the two clause BSD licence below.
#
# Copyright (c) 2007-2024 by the Sphinx team (see AUTHORS file). All rights reserved.
# Copyright 2024 NXP
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
import yaml,json
from sphinx.cmd.build import get_parser
import sphinx_rtd_theme
from functools import reduce
from pprint import pprint
import chardet,configparser

# -- MCUXpresso SDK Configuration Data ----------------------------------------
SDK_BASE = Path(__file__).absolute().parents[1]


# Patch the example_board_readme.md to avoid the warning
# WARNING: document isn't included in any toctree
def patch_example_readme_md(app, docname, source):
    if docname.endswith('example_board_readme'):
        source[0] = f'''---
orphan: true
---

{source[0]}
'''


def setup(app):
    app.connect('source-read', patch_example_readme_md)

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def list_md_files(entry_file, visited_files=None):
    '''Search all the md files refered by entry_file recursively'''

    if not visited_files:
        visited_files = set()

    if entry_file in visited_files:
        return

    visited_files.add(entry_file)

    with open(entry_file, encoding=detect_encoding(entry_file)) as fd:
        data = fd.read()

    references = re.findall(r'\[.*?\]\((.*?\.md\b)(?:#.*)?\)', data)

    for ref in references:
        ref_path = (entry_file.parent / Path(ref)).resolve()
        if ref_path.is_file():
            list_md_files(ref_path, visited_files)

    return visited_files


def expand_example_scope(example_scope):
    '''Expand the required md files and index.rst files to a list'''

    sdk_base      = SDK_BASE.resolve()
    example_scope = (sdk_base / Path(example_scope)).resolve()
    result        = set()

    if example_scope.is_dir():
        md_entries = example_scope.rglob('readme.md')
        result     = set([example_scope / '**' / 'index.rst', ])
    elif example_scope.is_file():
        md_entries = [example_scope, ]
    else:
        print(f'ERROR: Invalid example scope: {example_scope}')
        return []

    # Append md files
    result = reduce(lambda acc, x: acc.union(list_md_files(x.resolve())), md_entries, result)
    result = [str(x.relative_to(sdk_base)) for x in result]

    return result


class MCUXDocConfig:
    '''MCUXpresso SDK Configuration Data Class to simplify the feeding of configuration data'''
    NAME = 'default'
    def __init__(self, user_tags, example_scope=''):
        # Read the user config
        with open(SDK_BASE / 'docs' / '_cfg' / 'user_config.yml', 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        # If example_scope is specified through command line, use it.
        if example_scope != '':
            example_doc_files = expand_example_scope(example_scope)
            print('-' * 100)
            print("Files used for example readme generation")
            pprint(example_doc_files)
            print('-' * 100)

            self.config['modules']['examples']['external_contents'] = [
                { 'root': '.', 'pattern': x } for x in example_doc_files
            ]

        # Find matched tags
        self.user_tags = user_tags
        print('-- Collecting MCUXDocConfig Tags')
        for tag in self.user_tags:
            print(f'  [+] {tag}')

        if self.is_internal_doc:
            print('-- Creating Internal Document')
        else:
            print('-- Creating External Document')

        print('-- Collecting User Modules')
        # Match with module tag
        self.module_tags = []
        for module_name, _ in self.iter_configs():
            if any([re.fullmatch(tag, module_name) for tag in self.user_tags]):
                self.module_tags.append(module_name)
        if not self.module_tags:
            for module_name, module_config in self.iter_configs():
                if module_config.get('default', False):
                    self.module_tags.append(module_name)
        for module in self.module_tags:
            print(f'  [+] {module}')
        
        #collect URL map
        self.url_map = {}
        if self.is_internal_doc:
            internal_config = os.path.join(SDK_BASE, "..", "bifrost", ".gitconfig")
            if os.path.exists(internal_config):
                config = configparser.ConfigParser(strict=False)
                config.read(internal_config)
                for section in config.sections():
                    for key, value in config.items(section):
                        match = re.search(r'(?P<server_url>.+)/(?P<project>.+)/(?P<reponame>.+).git', section.replace("url ","").strip('"'))
                        server_url = match.group("server_url").replace("ssh://git@","https://")
                        project = match.group("project")
                        reponame = match.group("reponame")
                        self.url_map[value] = f'{server_url}/projects/{project.upper()}/repos/{reponame}'

    def iter_configs(self):
        for module_name, module_config in self.config['modules'].items():
            yield module_name, module_config

    @property
    def is_internal_doc(self):
        return bool('internal_doc' in self.user_tags)

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
        with open(SDK_BASE / "MCUX_VERSION", encoding='utf-8') as f:
            m = re.match(
                (
                    r"^CURRENT_YEAR\s*=\s*(\d+)$\n"
                    + r"^VERSION_MAJOR\s*=\s*(\d+)$\n"
                    + r"^VERSION_MINOR\s*=\s*([\d]+(-pvw\d+)*)$\n"
                ),
                f.read(),
                re.MULTILINE,
            )

            if not m:
                sys.stderr.write("Warning: Could not extract SDK version\n")
                matched_version = "Unknown"
            else:
                year, major, minor, preview = m.groups(1)
                matched_version= ".".join((year, major, minor))

        return matched_version

    def iter_modules(self):
        for module_name in self.module_tags:
            module_config = self.config['modules'][module_name]
            yield module_name, module_config

    def get_mod_config(self, mod_name, mod_config, key):
        # Get the module extenral config
        mod_option = mod_config.get(key, [])
        if mod_option:
            print(f'  [+] [external][{key}][{mod_name}]')

        # Get the internal module
        int_mod_config = mod_config.get('internal', {})
        if self.is_internal_doc and int_mod_config and int_mod_config.get(key, []):
            print(f'  [+] [internal][{key}][{mod_name}]')
            mod_option.extend(int_mod_config.get(key, []))

        return mod_option

    @property
    def extensions(self):
        print('-- Collect Extensions')
        my_extensions = self.config['extensions']

        if self.is_run_doxygen:
            my_extensions.extend(self.config["doxygen"]["extensions"])

        for module_name, module_config in self.iter_modules():
            mod_extensions = self.get_mod_config(module_name, module_config, 'extensions')
            my_extensions.extend(mod_extensions)

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
            mod_contents = self.get_mod_config(module_name, module_config, 'external_contents')
            contents.extend(
                [
                    (SDK_BASE/item['root'], item['pattern']) for item in mod_contents
                ]
            )

        return contents

    @property
    def external_content_keep(self):
        return []

    def get_repo_url(self, mod_vcs):
        if not self.url_map:
            return mod_vcs
        else:
            mod_vcs["link"] = self.url_map[mod_vcs["link"].rstrip('/')]
    @property
    def vcs_link(self):
        print('-- Collect VCS Link')
        from west.manifest import Manifest
        manifest = Manifest.from_topdir(topdir=os.path.dirname(SDK_BASE))
        links = []
        manifest_dict = manifest.as_dict()
        for sdk_prj in manifest_dict["manifest"]["projects"]:
            if sdk_prj["name"] == "mcu-sdk-doc":
                continue
            else:
                if "path" in sdk_prj.keys():
                    sdk_relpath = sdk_prj["path"].replace("mcuxsdk/","")
                    links.append(
                    { "pattern" : "/".join([sdk_relpath.rstrip("/"),"*"]),
                      "replace_prefix" : sdk_relpath.rstrip("/")+"/",
                      "link" : sdk_prj["url"].rstrip('/'),
                      "rev_branch": sdk_prj["userdata"]["track_branch"]
                    }
                    )

        links.append(
           self.config.get('vcs_link', {})
        )

        for link in links:
            self.get_repo_url(link)
        
        print(f"VCS links {links}")
        return links

    def doxygen_projects(self):
        print('-- Collect information for doxygen projects')
        doxygen_dicts = {}

        for module_name, module_config in self.iter_modules():
            mod_doxygen = self.get_mod_config(module_name, module_config, 'doxygen_runner')
            if mod_doxygen:
                doxygen_dicts[module_name] = mod_doxygen

        if self.config.get('doxygen_runner'):
            doxygen_dicts["common"] = self.config.get('doxygen_runner')

        # update path for the config
        for mod_name, mod_doxygen in doxygen_dicts.items():
            mod_doxygen["doxyfile"] = os.path.join(SDK_BASE, mod_doxygen["doxyfile"])
            mod_doxygen["outdir"] = os.path.join(DOC_BUILD, "doxygen", mod_doxygen["outdir"])
        
        print(f"doxygen projects {doxygen_dicts}")
        return doxygen_dicts


    @property
    def is_run_doxygen(self):
        return bool('doxygen' in self.user_tags)

args = get_parser().parse_args()

# Extract the -D parameters
d_params = {}
if args.define:
    for item in args.define:
        key, value = item.split('=', 1)
        d_params[key] = value

example_scope = d_params.get('example_scope', '')

mcux_config = MCUXDocConfig(tags, example_scope)  # pylint: disable=undefined-variable

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

# SDK_BASE = search_sdk_base()
DOC_BASE = SDK_BASE / "docs"
DOC_BUILD = Path(args.outputdir).resolve().parents[0]
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, str(DOC_BASE))
sys.path.insert(0, str(DOC_BASE / "_extensions"))

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

if 'doxyrunner' in extensions and mcux_config.is_run_doxygen:
    doxyrunner_doxygen = os.environ.get("DOXYGEN_EXECUTABLE", "doxygen")
    doxyrunner_doxydicts = mcux_config.doxygen_projects()
    # doxyrunner_doxyfile = DOC_BASE / "drivers" / "Doxyfile_lib_PDF_RM_Drivers"
    # doxyrunner_outdir = DOC_BUILD / "doxygen"
    doxyrunner_fmt = True
    doxyrunner_fmt_vars = {"SDK_BASE": str(SDK_BASE)}
    doxyrunner_outdir_var = "DOXY_OUT"

    # print(f"doxygen runner configuration: {doxyrunner_outdir}")
    # Breathe Configuration
    breathe_projects = {}
    print(doxyrunner_doxydicts)
    
    default_project=""
    for mod_name, mod_doxygen in doxyrunner_doxydicts.items():
        if not default_project:
            default_project = mod_name
        breathe_projects[mod_name] = f'{mod_doxygen["outdir"]}/xml'
        print(f'breathe_projects[{mod_name}] = {mod_doxygen["outdir"]}/xml')
    
    breathe_default_project = default_project
    breathe_separate_member_pages = True

    breathe_domain_by_extension = {
    "h": "c",
    "c": "c",
   }

#set up inline comments
comments_config = {
   "dokieli": True
}
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
    'navigation_depth': 5,
    "prev_next_buttons_location": None,
    'collapse_navigation' : True,
}
html_baseurl = "https://kex-dev.nxp.com/docs/latest/"
html_title = "MCUXpresso SDK Documentation"
static_path = [str(DOC_BASE / "_static")]
if os.path.exists(os.path.join(DOC_BASE, "internal")):
    static_path.append(str(DOC_BASE / "internal" / "public"))
    html_logo = str(DOC_BASE / "internal" / "images" / "nxp_logo_small.png")
    html_favicon = str(DOC_BASE / "internal" / "images" / "nxp_logo_small.png")
html_static_path = static_path
html_last_updated_fmt = "%b %d, %Y %H:%M%z"
html_domain_indices = False
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
docgen_branch = os.getenv("DOCGEN_BRANCH")
docgen_rev = os.getenv("DOCGEN_REV")
html_css_files = [
    'custom.css',
]

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
    "display_vcs_link": True,
}

is_internal_doc = mcux_config.is_internal_doc
with open(DOC_BASE / "versions.json", "r", encoding="utf-8") as f:
    versions_data = json.load(f)
if is_internal_doc:
    version_list = [(version, f"/mcuxsdk-internal/{version}/html/") for version in versions_data]
else:
    version_list = [(version, f"/mcuxsdk/{version}/html/") for version in versions_data]
    
html_context["versions"] = tuple(version_list)


# -- Options for vcs_link ------------------------------------------
if 'vcs_link' in extensions:
    vcs_link_prefixes = mcux_config.vcs_link
    vcs_link_version = f"release/{version}" if is_release else "main"


# -- Options for zephyr.external_content ----------------------------------
if 'external_content' in extensions:
    external_content_contents = mcux_config.external_content_contents
    external_content_keep = mcux_config.external_content_keep

suppress_warnings = [
    "myst.header", # WARNING: Non-consecutive header level increase; H4 to H7 [myst.header]
]
