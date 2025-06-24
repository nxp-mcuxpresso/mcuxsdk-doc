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
import chardet,fnmatch
from sphinx.util import logging

# -- MCUXpresso SDK Configuration Data ----------------------------------------
SDK_BASE = Path(__file__).absolute().parents[1]

logger = logging.getLogger("sphinx.config")

# Patch the example_board_readme.md to avoid the warning
# WARNING: document isn't included in any toctree
def patch_example_readme_md(app, docname, source):
    if docname.endswith('example_board_readme') or docname.find('ChangeLog_') != -1 or docname.find('commonrn') != -1:
        source[0] = f'''---
orphan: true
---

{source[0]}
'''

def read_file(filename):
    content = ""
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()

    return content

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
        logger.error(f'ERROR: Invalid example scope: {example_scope}')
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

        # Delete the mpp related configuration as workaround for pdf generation
        if os.environ.get('SPHINX_TARGET') == 'PDF':
            print("delete mpp documentation for pdf generation as workaround")
            for index, file_pattern in enumerate(self.config['modules']['mid_eiq']['external_contents']):
                print(f"{index} {file_pattern}")
                if "eiq/mpp" in file_pattern["pattern"]:
                    del self.config['modules']['mid_eiq']['external_contents'][index]
            

        # If example_scope is specified through command line, use it.
        if example_scope != '':
            example_doc_files = expand_example_scope(example_scope)
            logger.debug('-' * 100)
            logger.debug("Files used for example readme generation")
            pprint(example_doc_files)
            logger.debug('-' * 100)

            self.config['modules']['examples']['external_contents'] = [
                { 'root': '.', 'pattern': x } for x in example_doc_files
            ]

        # Find matched tags
        self.user_tags = user_tags
        logger.info('-- Collecting MCUXDocConfig Tags')
        for tag in self.user_tags:
            logger.info(f'  [+] {tag}')

        if self.is_internal_doc:
            logger.info('-- Creating Internal Document')
        else:
            logger.info('-- Creating External Document')

        logger.info('-- Collecting User Modules')
        # Match with module tag
        self.module_tags = []
        for module_name, module_config in self.iter_configs():
            if any([re.fullmatch(tag, module_name) for tag in self.user_tags]):
                self.module_tags.append(module_name)
                if module_config.get('doxygen_runner', False):
                    self.user_tags.add('doxygen')

        if not self.module_tags:
            for module_name, module_config in self.iter_configs():
                if module_config.get('default', False):
                    self.module_tags.append(module_name)
                    if module_config.get('doxygen_runner', False):
                        self.user_tags.add('doxygen')
        
        for module in self.module_tags:
            logger.info(f'  [+] {module}')
        
        #collect URL map
        self.url_map = {}
        if self.is_internal_doc:
            internal_config = os.path.join(SDK_BASE, "..", "bifrost", ".gitconfig")
            if os.path.exists(internal_config):
                for url, insteadOf in re.findall(r'\[url "(?P<url>[^"]+)"\]\s+insteadOf = (?P<insteadOf>[^\s]+)', read_file(internal_config), re.MULTILINE):
                    match = re.search(r'(?P<server_url>.+)/(?P<project>.+)/(?P<reponame>.+).git',url)
                    server_url = match.group("server_url").replace("ssh://git@","https://")
                    project = match.group("project")
                    reponame = match.group("reponame")
                    internal_url = f'{server_url}/projects/{project.upper()}/repos/{reponame}'
                    if insteadOf.endswith('.git'):
                        self.url_map[insteadOf.replace('.git', '').rstrip('/')] = internal_url
                    else:
                        self.url_map[insteadOf.rstrip('/')] = internal_url
        #print(f'URL Map: {self.url_map}')
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
            logger.info(f'  [+] [external][{key}][{mod_name}]')

        # Get the internal module
        int_mod_config = mod_config.get('internal', {})
        if self.is_internal_doc and int_mod_config and int_mod_config.get(key, []):
            logger.info(f'  [+] [internal][{key}][{mod_name}]')
            mod_option.extend(int_mod_config.get(key, []))

        return mod_option

    @property
    def extensions(self):
        logger.info('-- Collect Extensions')
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
        logger.debug('-- Collect External Content')
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
        #print('-- Collect VCS Link')
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
        
        logger.debug(f"VCS links {links}")
        return links

    def doxygen_projects(self):
        logger.debug('-- Collect information for doxygen projects')
        doxygen_dicts = {}

        for module_name, module_config in self.iter_modules():
            mod_doxygen = self.get_mod_config(module_name, module_config, 'doxygen_runner')
            if mod_doxygen:
                doxygen_name = module_name
                if mod_doxygen["outdir"].startswith("drivers"):
                    doxygen_name = mod_doxygen["outdir"].replace("/","_")
                if doxygen_name not in doxygen_dicts.keys():
                    doxygen_dicts[doxygen_name] = mod_doxygen

        if self.config.get('doxygen_runner'):
            doxygen_dicts["common"] = self.config.get('doxygen_runner')

        # update path for the config
        for mod_name, mod_doxygen in doxygen_dicts.items():
            mod_doxygen["doxyfile"] = os.path.join(SDK_BASE, mod_doxygen["doxyfile"])
            mod_doxygen["outdir"] = os.path.join(DOC_BUILD, "doxygen", mod_doxygen["outdir"])
        
        logger.debug(f"doxygen projects {doxygen_dicts}")
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

# Add board_target configuration
logger.debug(f"{d_params}")
board_target = d_params.get('board_target', None)
if board_target:
    logger.debug(f"-- Building documentation for board target: {board_target}")
    
    # Determine board family and path
    board_parts = board_target.split('/')
    if len(board_parts) == 2:
        board_family, board_name = board_parts
        board_path = f"boards/{board_family}/{board_name}"
        logger.debug(f"-- Board path: {board_path}")
    else:
        board_family = None
        board_name = board_target
        # Try to find the board in all families
        for family in ["DSC", "i.MX", "RT", "Kinetis", "LPC", "MCX", "Wireless"]:
            potential_path = f"boards/{family}/{board_name}"
            if (SDK_BASE / "docs" / potential_path).exists():
                board_family = family
                board_path = potential_path
                logger.debug(f"-- Found board in family {board_family}, path: {board_path}")
                break
        
        if not board_family:
            logger.warn(f"-- Warning: Could not determine board family for {board_name}")
            board_path = None
    
    # Filter user configuration based on board target
    if board_path and (SDK_BASE / "docs" / board_path).exists():
        # Load user config to get module patterns
        user_config_path = os.path.join(SDK_BASE, "docs", "_cfg", "user_config.yml")
        with open(user_config_path, encoding='utf-8') as f:
            user_config = yaml.safe_load(f)
        
        # Initialize sets to track files and modules
        included_files = set()
        included_modules = set([f'board_{board_name}'])  # Always include these
        processed_files = set()
        
        def add_processed_files(file_path):
            if not file_path.exists():
                return False

            if str(file_path).startswith(str(SDK_BASE / "docs")):
                if str(file_path.relative_to(SDK_BASE / "docs")) in processed_files:
                    return False
                processed_files.add(str(file_path.relative_to(SDK_BASE / "docs")))
                included_files.add(str(file_path.relative_to(SDK_BASE / "docs")))
            else:
                if str(file_path.relative_to(SDK_BASE)) in processed_files:
                    return False
                processed_files.add(str(file_path.relative_to(SDK_BASE )))
                included_files.add(str(file_path.relative_to(SDK_BASE)))
            
            return True

        # Function to process a file and find dependencies
        def process_file(file_path, is_board_file=False):
            if not add_processed_files(file_path):
                return

            logger.debug(f"-- Processing file: {file_path}")
            
            # Read the file content
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                logger.error(f"-- Error reading {file_path}: {e}")
                return
            
            # Find toctree entries
            if file_path.suffix == '.rst':
                toctree_pattern = re.compile(r'^\.\. toctree::(.*?)(?=^\S|\Z)', re.MULTILINE | re.DOTALL)
                for toctree_match in toctree_pattern.finditer(content):
                    toctree_content = toctree_match.group(1)
                    
                    # Extract file paths from the toctree
                    lines = toctree_content.strip().split('\n')
                    for line in lines:
                        line = line.strip()
                        if line and not line.startswith(':') and not line.startswith('#'):
                            # Resolve the path relative to the current file
                            ref_path = resolve_path(file_path.parent, line)
                            if ref_path:
                                process_file(ref_path, is_board_file)
            
                # Find :ref: references
                ref_pattern = re.compile(r':ref:`([^`]+)`')
                for ref_match in ref_pattern.finditer(content):
                    ref_name = ref_match.group(1)
                    
                    # Special case for freertos
                    if ref_name in user_config["modules"]:
                        included_modules.add(ref_name)
                    
                    # Find the file that defines the reference
                    ref_file = find_ref_file(ref_name)

                    if ref_file:
                        #only search for index, no recursively search
                        if "index" not in ref_file.name:
                            add_processed_files(ref_file)
                        else:
                            process_file(ref_file, is_board_file)

                # Find :ref: references
                doc_pattern = re.compile(r':doc:`([^`]+)`')
                for doc_match in doc_pattern.finditer(content):
                    doc_path = doc_match.group(1).split('<')[-1].split('>')[0]
                    ref_path = resolve_path(file_path.parent, doc_path)
                    if ref_path:
                        process_file(ref_path, is_board_file)
            
        
            # Find markdown link files
            if file_path.suffix == '.md':
                
                # Find all markdown links [text](link)
                md_link_pattern = r'\[.*?\]\((.*?)(?:\s.*?)?\)'
                for md_link_match in re.finditer(md_link_pattern, content):
                    link = md_link_match.group(1).strip()
                    # Ignore external links and anchors
                    if not link.startswith(('http://', 'https://', '#')):
                        link_path = link.split('#')[0]
                        # Resolve the path relative to the current file
                        ref_path = resolve_path(file_path.parent, link_path)
                        if ref_path:
                            process_file(ref_path, is_board_file)

                # Find all include markdown files with syntax {include}
                md_include_pattern = r'\{include\}(\s*.*)'
                for md_include_match in re.finditer(md_include_pattern, content):
                    md_include_path = md_include_match.group(1).strip()
                    # Resolve the path relative to the current file
                    ref_path = resolve_path(file_path.parent, md_include_path)
                    if ref_path:
                        process_file(ref_path, is_board_file)
                   
        # Function to resolve a path relative to a base directory
        def resolve_path(base_dir, path):
            path_ext = os.path.splitext(path)[1]
            if path_ext not in ['.rst', '.md', '']:
                return None

            # Try with different extensions
            for ext in ['.rst', '.md', '']:
                full_path = (base_dir / f"{path}{ext}").resolve()
                if full_path.exists():
                    return full_path

            # If not found, try modified base_dir point to SDK_BASE as parent
            base_dir = Path(str(base_dir).replace(str(SDK_BASE / "docs"), str(SDK_BASE)))
            for ext in ['.rst', '.md', '']:
                full_path = (base_dir / f"{path}{ext}").resolve()
                if full_path.exists():
                    return full_path
            
            # If not found, try as an absolute path from docs directory
            for ext in ['.rst', '.md', '']:
                full_path = (SDK_BASE / "docs" / f"{path.lstrip('/')}{ext}").resolve()
                if full_path.exists():
                    return full_path

            # If not found, try as an absolute path from SDK_BASE directory
            for ext in ['.rst', '.md', '']:
                full_path = (SDK_BASE / f"{path.lstrip('/')}{ext}").resolve()
                if full_path.exists():
                    return full_path
            
            logger.error(f"-- Could not resolve path: {path} from {base_dir}")
            return None
        
        # Function to find the file that defines a reference
        def find_ref_file(ref_name):
            # Search for the reference in all .rst files
            for rst_file in (SDK_BASE).glob('**/*.rst'):
                try:
                    with open(rst_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if f".. _{ref_name}:" in content:
                            return rst_file
                except Exception as e:
                    logger.error(f"-- Error reading {rst_file}: {e}")
            
            logger.error(f"-- Could not find reference: {ref_name}")
            return None
        
        # Start with the board's index.rst
        board_index = SDK_BASE / "docs" / board_path / "index.rst"
        if board_index.exists():
            process_file(board_index, True)

        # Match files to modules
        run_doxygen = False
        device_path = "drivers"
        if 'modules' in user_config:
            for module_name, module_config in user_config['modules'].items():
                if 'external_contents' in module_config:
                    for content_config in module_config['external_contents']:
                        root = content_config.get('root', '.')
                        pattern = content_config.get('pattern', '')
                        glob_pattern = pattern

                        # Check if any included file matches this pattern
                        for file_path in included_files:
                            normalized_path = os.path.normpath(file_path)
                            normalized_pattern = os.path.normpath(glob_pattern)
                            logger.debug(f"-- Checking file: {normalized_path} against pattern: {normalized_pattern}")
                            if fnmatch.fnmatch(normalized_path, normalized_pattern):
                                included_modules.add(module_name)
                                if "doxygen_runner" in module_config:
                                    run_doxygen = True
                                    if module_config["doxygen_runner"]["outdir"].startswith("drivers"):
                                        #device_name = module_config["doxygen_runner"]["outdir"].replace("\\","/").split("/")[-1]
                                        device_path = module_config["doxygen_runner"]["outdir"].replace("\\","/")
                                break
        
        # Filter the tags parameter to include only board-related modules
        if 'tags' in d_params:
            all_modules = d_params['tags'].split(',')
            filtered_modules = [module for module in all_modules if module in included_modules]
        else:
            filtered_modules = included_modules
        d_params['tags'] = ','.join(filtered_modules)
        # if run_doxygen:
        #     d_params['tags'] = d_params['tags'] + ',doxygen'
        
        logger.info(f"-- Filtered modules for board {board_target}: {filtered_modules}")
        
        # Create a custom master document for board-specific builds
        master_doc = 'board_index'
        
        # Create a temporary index file that only includes the board documentation
        board_index_content = f"""
Board-Specific Documentation: {board_target}
=================================================

This documentation contains information specific to the {board_name} board.

.. toctree::
   :maxdepth: 1

   {board_path}/index
   {device_path}/index
   middleware/index
   rtos/index
"""
        logger.info(f"{board_index_content}") 
        
        # Write the temporary index file
        board_index_path = SDK_BASE / "docs" / "board_index.rst"
        with open(board_index_path, 'w') as f:
            f.write(board_index_content)
        
        # Set the master document
        d_params['master_doc'] = 'board_index'
        master_doc = 'board_index'

# Now initialize mcux_config with the filtered parameters

example_scope = d_params.get('example_scope', '')
for tag in d_params.get('tags', '').split(','):
    if not tags.has(tag):
        tags.add(tag)
        logger.debug(f"-- Adding tag: {tag}")

mcux_config = MCUXDocConfig(tags, example_scope)  # pylint: disable=undefined-variable

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

if board_target:
  latex_documents = [
    (master_doc, f"mcuxsdk-{board_target}.tex", "MCUXpresso SDK Documentation", author, "manual"),
]
else:
  latex_documents = [
    ("index-tex", "mcuxsdk.tex", "MCUXpresso SDK Documentation", author, "manual"),
]

latex_engine = "xelatex"

# -- Options for doxyrunner plugin ---------------------------------

if 'doxyrunner' in extensions and mcux_config.is_run_doxygen:
    doxyrunner_doxygen = os.environ.get("DOXYGEN_EXECUTABLE", "doxygen")
    doxyrunner_doxydicts = mcux_config.doxygen_projects()
    doxyrunner_fmt = True
    doxyrunner_fmt_vars = {"SDK_BASE": str(SDK_BASE)}
    doxyrunner_outdir_var = "DOXY_OUT"

    breathe_projects = {}
    print(doxyrunner_doxydicts)
    
    default_project=""
    for mod_name, mod_doxygen in doxyrunner_doxydicts.items():
        if not default_project:
            default_project = mod_name
        breathe_projects[mod_name] = f'{mod_doxygen["outdir"]}/xml'
        logger.debug(f'breathe_projects[{mod_name}] = {mod_doxygen["outdir"]}/xml')
    
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
    'image.fetch'
]
# suppress_warnings = ['image.fetch']
# conf.py
image_fetch_timeout = 1  # Timeout in seconds
myst_heading_anchors = 6
#myst_all_links_external = False