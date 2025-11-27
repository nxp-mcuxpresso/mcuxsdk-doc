"""
Configuration Manager for MCUXpresso SDK Documentation
Copyright 2025 NXP
SPDX-License-Identifier: BSD-3-Clause

This module provides a centralized configuration management system
that handles board-specific filtering, module selection, and build
mode configuration.

Key Concepts:
- Build modes (original/html/sphinx) ONLY affect driver doxygen projects
- Non-driver projects follow their configuration in user_config.yml
- PDF/LaTeX builds force all projects to use breathe mode
- Multiple doxygen modes can coexist in the same build
"""

import os
import re
import yaml
import fnmatch
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from sphinx.util import logging

logger = logging.getLogger("config_manager")


class ConfigurationManager:
    """
    Centralized configuration manager for MCUXpresso SDK documentation.
    Handles build mode selection, board filtering, and module configuration.
    """
    
    def __init__(self, sdk_base: Path, user_tags, example_scope='', 
                 build_mode='sphinx', board_target=None):
        self.sdk_base = sdk_base
        self.user_tags = user_tags
        self.example_scope = example_scope
        self.board_target = board_target
        
        # Detect if we're building PDF/LaTeX
        sphinx_target = os.environ.get('SPHINX_TARGET', '').upper()
        self.is_pdf_build = sphinx_target in ['PDF', 'LATEX']
        
        # Store the requested build mode (only affects driver projects)
        self.driver_build_mode = build_mode
        
        if self.is_pdf_build:
            logger.warning(
                f"PDF/LaTeX build detected. All doxygen projects will use breathe mode "
                f"(driver_build_mode '{build_mode}' will be ignored for this build)."
            )
        else:
            logger.info(f"Driver doxygen projects will use: {build_mode} mode")
        
        # Load configuration
        config_file = sdk_base / 'docs' / '_cfg' / 'user_config.yml'
        logger.info(f"Loading configuration from: {config_file}")
        
        with open(config_file, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        # PDF workaround: remove mpp documentation
        if self.is_pdf_build:
            logger.info("PDF build: Removing MPP documentation as workaround")
            if 'mid_eiq' in self.config.get('modules', {}):
                external_contents = self.config['modules']['mid_eiq'].get('external_contents', [])
                self.config['modules']['mid_eiq']['external_contents'] = [
                    item for item in external_contents 
                    if 'eiq/mpp' not in item.get('pattern', '')
                ]
        
        # Handle example scope
        if example_scope:
            example_files = self._expand_example_scope(example_scope)
            self.config['modules']['examples']['external_contents'] = [
                {'root': '.', 'pattern': x} for x in example_files
            ]
        
        # Collect module tags
        self._collect_module_tags()
        
        # Handle board-specific filtering
        if board_target:
            self._filter_for_board()
        
        # Collect URL map for internal docs
        self._collect_url_map()
    
    def _collect_module_tags(self):
        """Collect module tags based on user tags."""
        logger.info('-- Collecting MCUXDocConfig Tags')
        for tag in self.user_tags:
            logger.info(f'  [+] {tag}')
        
        if self.is_internal_doc:
            logger.info('-- Creating Internal Document')
        else:
            logger.info('-- Creating External Document')
        
        logger.info('-- Collecting User Modules')
        self.module_tags = []
        
        # Match with module tag
        for module_name, module_config in self.config.get('modules', {}).items():
            if any(re.fullmatch(tag, module_name) for tag in self.user_tags):
                self.module_tags.append(module_name)
                if module_config.get('doxygen_runner', False):
                    self.user_tags.add('doxygen')
        
        # Add default modules if no matches
        if not self.module_tags:
            for module_name, module_config in self.config.get('modules', {}).items():
                if module_config.get('default', False):
                    self.module_tags.append(module_name)
                    if module_config.get('doxygen_runner', False):
                        self.user_tags.add('doxygen')
        
        for module in self.module_tags:
            logger.info(f'  [+] {module}')
    
    def _filter_for_board(self):
        """Filter configuration for board-specific build."""
        logger.info(f"Filtering configuration for board: {self.board_target}")
        
        resolver = BoardDependencyResolver(self.sdk_base, self.board_target)
        included_files, included_modules = resolver.resolve(self.config)
        
        # Always include the board module itself
        board_module = f'board_{self.board_target.split("/")[-1]}'
        included_modules.add(board_module)
        
        # Filter module tags
        self.module_tags = [m for m in self.module_tags if m in included_modules]
        
        logger.info(f"Filtered modules for board {self.board_target}: {self.module_tags}")
    
    def _expand_example_scope(self, example_scope: str) -> List[str]:
        """Expand example scope to list of files."""
        from functools import reduce
        
        example_scope_path = (self.sdk_base / Path(example_scope)).resolve()
        result = set()
        
        if example_scope_path.is_dir():
            md_entries = example_scope_path.rglob('readme.md')
            result = set([example_scope_path / '**' / 'index.rst'])
        elif example_scope_path.is_file():
            md_entries = [example_scope_path]
        else:
            logger.error(f'Invalid example scope: {example_scope}')
            return []
        
        # Append md files
        result = reduce(
            lambda acc, x: acc.union(self._list_md_files(x.resolve())), 
            md_entries, 
            result
        )
        result = [str(x.relative_to(self.sdk_base)) for x in result]
        
        return result
    
    def _list_md_files(self, entry_file: Path, visited_files=None) -> Set[Path]:
        """Search all md files referenced by entry_file recursively."""
        if visited_files is None:
            visited_files = set()
        
        if entry_file in visited_files:
            return visited_files
        
        visited_files.add(entry_file)
        
        try:
            with open(entry_file, 'r', encoding='utf-8') as f:
                data = f.read()
        except Exception as e:
            logger.error(f"Error reading {entry_file}: {e}")
            return visited_files
        
        references = re.findall(r'\[.*?\]\((.*?\.md\b)(?:#.*)?\)', data)
        
        for ref in references:
            ref_path = (entry_file.parent / Path(ref)).resolve()
            if ref_path.is_file():
                self._list_md_files(ref_path, visited_files)
        
        return visited_files
    
    def _collect_url_map(self):
        """Collect URL mappings for internal documentation."""
        self.url_map = {}
        
        if not self.is_internal_doc:
            return
        
        internal_config = self.sdk_base.parent / "bifrost" / ".gitconfig"
        if not internal_config.exists():
            return
        
        try:
            with open(internal_config, 'r', encoding='utf-8') as f:
                content = f.read()
            
            pattern = r'\[url "(?P<url>[^"]+)"\]\s+insteadOf = (?P<insteadOf>[^\s]+)'
            for url, insteadOf in re.findall(pattern, content, re.MULTILINE):
                match = re.search(
                    r'(?P<server_url>.+)/(?P<project>.+)/(?P<reponame>.+).git',
                    url
                )
                if match:
                    server_url = match.group("server_url").replace("ssh://git@", "https://")
                    project = match.group("project")
                    reponame = match.group("reponame")
                    internal_url = f'{server_url}/projects/{project.upper()}/repos/{reponame}'
                    
                    key = insteadOf.replace('.git', '').rstrip('/')
                    self.url_map[key] = internal_url
        except Exception as e:
            logger.error(f"Error reading internal config: {e}")
    
    @property
    def is_internal_doc(self) -> bool:
        """Check if building internal documentation."""
        return 'internal_doc' in self.user_tags
    
    @property
    def project(self) -> str:
        """Get project name."""
        return self.config.get('project', 'mcuxsdk')
    
    @property
    def copyright(self) -> str:
        """Get copyright string."""
        return self.config.get('copyright', '2021,2025, NXP')
    
    @property
    def author(self) -> str:
        """Get author string."""
        return self.config.get('author', 'NXP')
    
    @property
    def version(self) -> str:
        """Get SDK version."""
        version_file = self.sdk_base / "MCUX_VERSION"
        
        try:
            with open(version_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            pattern = (
                r"^CURRENT_YEAR\s*=\s*(\d+)$\n"
                r"^VERSION_MAJOR\s*=\s*(\d+)$\n"
                r"^VERSION_MINOR\s*=\s*([\d]+(-pvw\d+)*)$\n"
            )
            match = re.match(pattern, content, re.MULTILINE)
            
            if match:
                year, major, minor, _ = match.groups()
                return ".".join((year, major, minor))
        except Exception as e:
            logger.error(f"Error reading version: {e}")
        
        return "Unknown"
    
    def get_extensions(self) -> List[str]:
        """
        Get list of Sphinx extensions.
        
        Extensions are determined by:
        1. Base extensions from user_config.yml
        2. Doxygen extensions based on what modes are needed
        3. Module-specific extensions
        """
        logger.info('-- Collecting Extensions')
        extensions = self.config.get('extensions', []).copy()
        
        # Determine which doxygen extensions are needed
        needed_extensions = self._determine_needed_doxygen_extensions()
        
        logger.info(f'-- Doxygen extensions needed: {needed_extensions}')
        
        # Add needed doxygen extensions
        for ext in needed_extensions:
            if ext not in extensions:
                extensions.append(ext)
        
        # Add module-specific extensions
        for module_name in self.module_tags:
            module_config = self.config['modules'][module_name]
            mod_extensions = self._get_mod_config(module_name, module_config, 'extensions')
            for ext in mod_extensions:
                if ext not in extensions:
                    extensions.append(ext)
        
        logger.info(f'-- Final extensions: {extensions}')
        return extensions
    
    def _determine_needed_doxygen_extensions(self) -> Set[str]:
        """
        Determine which doxygen extensions are needed based on project configurations.
        
        Returns a set of extension names needed.
        """
        needed = set()
        
        if not self.has_doxygen_projects:
            return needed
        
        # Check each module's doxygen configuration
        for module_name in self.module_tags:
            module_config = self.config['modules'][module_name]
            doxy_config = self._get_mod_config(module_name, module_config, 'doxygen_runner')
            
            if not doxy_config:
                continue
            
            is_driver = doxy_config.get("outdir", "").startswith("drivers")
            
            # Determine which mode this project should use
            if self.is_pdf_build:
                # PDF: everything uses breathe
                needed.add('breathe')
                needed.add('doxyrunner')
            elif is_driver:
                # Driver project: use driver_build_mode
                if self.driver_build_mode == 'html':
                    needed.add('doxyrunner_html')
                elif self.driver_build_mode == 'sphinx':
                    needed.add('doxyrunner_sphinx')
                else:  # original
                    needed.add('breathe')
                    needed.add('doxyrunner')
            else:
                # Non-driver project: check user_config.yml for preferred mode
                # Default to breathe if not specified
                preferred_mode = doxy_config.get('mode', 'breathe')
                
                if preferred_mode == 'html':
                    needed.add('doxyrunner_html')
                elif preferred_mode == 'sphinx':
                    needed.add('doxyrunner_sphinx')
                else:  # breathe or original
                    needed.add('breathe')
                    needed.add('doxyrunner')
        
        # Check global doxygen config
        if self.config.get('doxygen_runner'):
            global_mode = self.config['doxygen_runner'].get('mode', 'breathe')
            if self.is_pdf_build:
                needed.add('breathe')
                needed.add('doxyrunner')
            elif global_mode == 'html':
                needed.add('doxyrunner_html')
            elif global_mode == 'sphinx':
                needed.add('doxyrunner_sphinx')
            else:
                needed.add('breathe')
                needed.add('doxyrunner')
        
        return needed
    
    def get_source_suffix(self) -> Dict[str, str]:
        """Get source file suffix mappings."""
        return self.config.get('source_suffix', {})
    
    def get_external_contents(self) -> List[Tuple[Path, str]]:
        """Get external content configurations."""
        logger.debug('-- Collecting External Content')
        
        contents = [
            (self.sdk_base / item['root'], item['pattern']) 
            for item in self.config.get('external_contents', [])
        ]
        
        for module_name in self.module_tags:
            module_config = self.config['modules'][module_name]
            mod_contents = self._get_mod_config(module_name, module_config, 'external_contents')
            contents.extend([
                (self.sdk_base / item['root'], item['pattern']) 
                for item in mod_contents
            ])
        
        return contents
    
    def get_vcs_links(self) -> List[Dict]:
        """Get VCS link configurations."""
        try:
            from west.manifest import Manifest
            manifest = Manifest.from_topdir(topdir=str(self.sdk_base.parent))
            links = []
            manifest_dict = manifest.as_dict()
            
            for sdk_prj in manifest_dict["manifest"]["projects"]:
                if sdk_prj["name"] == "mcu-sdk-doc":
                    continue
                
                if "path" in sdk_prj:
                    sdk_relpath = sdk_prj["path"].replace("mcuxsdk/", "")
                    link_config = {
                        "pattern": "/".join([sdk_relpath.rstrip("/"), "*"]),
                        "replace_prefix": sdk_relpath.rstrip("/") + "/",
                        "link": sdk_prj["url"].rstrip('/'),
                        "rev_branch": sdk_prj["userdata"]["track_branch"]
                    }
                    self._apply_url_map(link_config)
                    links.append(link_config)
            
            # Add default VCS link
            default_link = self.config.get('vcs_link', {})
            self._apply_url_map(default_link)
            links.append(default_link)
            
            return links
        except Exception as e:
            logger.error(f"Error getting VCS links: {e}")
            return []
    
    def _apply_url_map(self, link_config: Dict):
        """Apply URL mapping for internal documentation."""
        if not self.url_map:
            return
        
        link = link_config.get("link", "")
        if "github.com" not in link:
            key = link.rstrip('/')
            if key in self.url_map:
                link_config["link"] = self.url_map[key]
    
    @property
    def has_doxygen_projects(self) -> bool:
        """Check if any modules have doxygen projects."""
        return 'doxygen' in self.user_tags
    
    def get_doxygen_projects_by_extension(self, doc_build: Path) -> Dict[str, List[Dict]]:
        """
        Get doxygen projects organized by which extension should handle them.
        
        Returns:
            Dict with keys: 'doxyrunner' (breathe), 'doxyrunner_html', 'doxyrunner_sphinx'
        """
        logger.info('-- Organizing Doxygen projects by extension')
        
        projects = {
            'doxyrunner': [],        # Projects using breathe (original mode)
            'doxyrunner_html': [],   # Projects using HTML mode
            'doxyrunner_sphinx': []  # Projects using Sphinx mode
        }
        
        for module_name in self.module_tags:
            module_config = self.config['modules'][module_name]
            doxy_config = self._get_mod_config(module_name, module_config, 'doxygen_runner')
            
            if not doxy_config:
                continue
            
            # Determine project name
            if doxy_config["outdir"].startswith("drivers"):
                project_name = doxy_config["outdir"].replace("/", "_").replace("\\", "_")
            else:
                project_name = module_name
            
            # Create project config
            project_info = {
                'name': project_name,
                'doxyfile': str(self.sdk_base / doxy_config["doxyfile"]),
                'outdir': str(doc_build / "doxygen" / doxy_config["outdir"]),
                'module': module_name
            }
            
            # Determine which extension should handle this project
            is_driver = doxy_config["outdir"].startswith("drivers")
            
            if self.is_pdf_build:
                # PDF: all projects use breathe
                extension_key = 'doxyrunner'
                logger.info(f"  PDF build: {project_name} -> doxyrunner (breathe)")
            elif is_driver:
                # Driver project: use driver_build_mode
                if self.driver_build_mode == 'html':
                    extension_key = 'doxyrunner_html'
                    logger.info(f"  Driver: {project_name} -> doxyrunner_html")
                elif self.driver_build_mode == 'sphinx':
                    extension_key = 'doxyrunner_sphinx'
                    logger.info(f"  Driver: {project_name} -> doxyrunner_sphinx")
                else:  # original
                    extension_key = 'doxyrunner'
                    logger.info(f"  Driver: {project_name} -> doxyrunner (breathe)")
            else:
                # Non-driver: check user_config.yml
                preferred_mode = doxy_config.get('mode', 'breathe')
                
                if preferred_mode == 'html':
                    extension_key = 'doxyrunner_html'
                    logger.info(f"  Non-driver: {project_name} -> doxyrunner_html (user config)")
                elif preferred_mode == 'sphinx':
                    extension_key = 'doxyrunner_sphinx'
                    logger.info(f"  Non-driver: {project_name} -> doxyrunner_sphinx (user config)")
                else:  # breathe
                    extension_key = 'doxyrunner'
                    logger.info(f"  Non-driver: {project_name} -> doxyrunner (breathe, user config)")
            
            projects[extension_key].append(project_info)
        
        # Add global doxygen config if exists
        if self.config.get('doxygen_runner'):
            global_config = self.config['doxygen_runner']
            common_info = {
                'name': 'common',
                'doxyfile': str(self.sdk_base / global_config['doxyfile']),
                'outdir': str(doc_build / "doxygen" / global_config['outdir']),
                'module': 'global'
            }
            
            if self.is_pdf_build:
                extension_key = 'doxyrunner'
            else:
                global_mode = global_config.get('mode', 'breathe')
                if global_mode == 'html':
                    extension_key = 'doxyrunner_html'
                elif global_mode == 'sphinx':
                    extension_key = 'doxyrunner_sphinx'
                else:
                    extension_key = 'doxyrunner'
            
            projects[extension_key].append(common_info)
            logger.info(f"  Global: common -> {extension_key}")
        
        # Log summary
        for ext_name, projs in projects.items():
            if projs:
                logger.info(f"  {ext_name}: {len(projs)} projects")
        
        return projects
    
    def get_breathe_projects(self, doc_build: Path) -> Dict[str, str]:
        """
        Get breathe project configurations.
        Only includes projects that use doxyrunner (breathe mode).
        """
        logger.debug('-- Collecting Breathe projects')
        breathe_projects = {}
        
        doxygen_projects = self.get_doxygen_projects_by_extension(doc_build)
        
        # Only projects in 'doxyrunner' use breathe
        for project in doxygen_projects['doxyrunner']:
            breathe_projects[project['name']] = f"{project['outdir']}/xml"
            logger.debug(f"  breathe_projects[{project['name']}] = {project['outdir']}/xml")
        
        return breathe_projects
    
    def get_master_doc(self) -> str:
        """Get the master document name."""
        if self.board_target:
            return 'board_index'
        return 'index'
    
    def create_board_index(self, doc_base: Path):
        """Create a temporary board index file."""
        if not self.board_target:
            return
        
        # Determine board path
        board_parts = self.board_target.split('/')
        if len(board_parts) == 2:
            board_family, board_name = board_parts
            board_path = f"boards/{board_family}/{board_name}"
        else:
            board_name = self.board_target
            # Find the board
            for family in ["DSC", "i.MX", "RT", "Kinetis", "LPC", "MCX", "Wireless"]:
                potential_path = f"boards/{family}/{board_name}"
                if (doc_base / potential_path).exists():
                    board_path = potential_path
                    break
            else:
                logger.error(f"Could not find board path for {board_name}")
                return
        
        # Find device path from modules
        device_path = "drivers"
        for module_name in self.module_tags:
            module_config = self.config['modules'].get(module_name, {})
            if 'doxygen_runner' in module_config:
                outdir = module_config['doxygen_runner']['outdir']
                if outdir.startswith("drivers"):
                    device_path = outdir.replace("\\", "/")
                    break
        
        # Create board index content
        board_index_content = f"""
Board-Specific Documentation: {self.board_target}
{'=' * (30 + len(self.board_target))}

This documentation contains information specific to the {board_name} board.

.. toctree::
   :maxdepth: 1

   {board_path}/index
   {device_path}/index
   middleware/index
   rtos/index
"""
        
        # Write the board index file
        board_index_path = doc_base / "board_index.rst"
        with open(board_index_path, 'w', encoding='utf-8') as f:
            f.write(board_index_content)
        
        logger.info(f"Created board index at {board_index_path}")
    
    def _get_mod_config(self, mod_name: str, mod_config: Dict, key: str):
        """Get module configuration for a specific key."""
        mod_option = mod_config.get(key, [] if key != 'doxygen_runner' else None)
        
        # Get internal module config if applicable
        int_mod_config = mod_config.get('internal', {})
        if self.is_internal_doc and int_mod_config and int_mod_config.get(key):
            logger.info(f'  [+] [internal][{key}][{mod_name}]')
            if isinstance(mod_option, list):
                mod_option.extend(int_mod_config.get(key, []))
            else:
                # For doxygen_runner, prefer internal config
                mod_option = int_mod_config.get(key, mod_option)
        
        return mod_option


class BoardDependencyResolver:
    """
    Resolves dependencies for board-specific documentation builds.
    """
    
    def __init__(self, sdk_base: Path, board_target: str):
        self.sdk_base = sdk_base
        self.board_target = board_target
        self.included_files: Set[str] = set()
        self.processed_files: Set[str] = set()
    
    def resolve(self, config: dict) -> Tuple[Set[str], Set[str]]:
        """Resolve all dependencies for a board."""
        logger.info(f"Resolving dependencies for board: {self.board_target}")
        
        # Find board path
        board_path = self._find_board_path()
        if not board_path:
            logger.error(f"Could not find board path for {self.board_target}")
            return set(), set()
        
        # Process board's index.rst
        board_index = self.sdk_base / "docs" / board_path / "index.rst"
        if board_index.exists():
            self._process_file(board_index)
        
        # Match files to modules
        included_modules = self._match_files_to_modules(config)
        
        return self.included_files, included_modules
    
    def _find_board_path(self) -> Optional[str]:
        """Find the path to the board documentation."""
        board_parts = self.board_target.split('/')
        
        if len(board_parts) == 2:
            return f"boards/{board_parts[0]}/{board_parts[1]}"
        
        # Search in all families
        board_name = self.board_target
        for family in ["DSC", "i.MX", "RT", "Kinetis", "LPC", "MCX", "Wireless"]:
            potential_path = f"boards/{family}/{board_name}"
            if (self.sdk_base / "docs" / potential_path).exists():
                logger.info(f"Found board in family {family}")
                return potential_path
        
        return None
    
    def _add_to_processed(self, file_path: Path) -> bool:
        """Add a file to the processed set."""
        if not file_path.exists():
            return False
        
        # Determine relative path
        if str(file_path).startswith(str(self.sdk_base / "docs")):
            rel_path = str(file_path.relative_to(self.sdk_base / "docs"))
        else:
            rel_path = str(file_path.relative_to(self.sdk_base))
        
        if rel_path in self.processed_files:
            return False
        
        self.processed_files.add(rel_path)
        self.included_files.add(rel_path)
        return True
    
    def _process_file(self, file_path: Path):
        """Process a file and find its dependencies."""
        if not self._add_to_processed(file_path):
            return
        
        logger.debug(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            logger.error(f"Error reading {file_path}: {e}")
            return
        
        if file_path.suffix == '.rst':
            self._process_rst_file(file_path, content)
        elif file_path.suffix == '.md':
            self._process_md_file(file_path, content)
    
    def _process_rst_file(self, file_path: Path, content: str):
        """Process RST file for dependencies."""
        # Find toctree entries
        toctree_pattern = re.compile(
            r'^\.\. toctree::(.*?)(?=^\S|\Z)', 
            re.MULTILINE | re.DOTALL
        )
        for match in toctree_pattern.finditer(content):
            toctree_content = match.group(1)
            lines = toctree_content.strip().split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith(':') and not line.startswith('#'):
                    ref_path = self._resolve_path(file_path.parent, line)
                    if ref_path:
                        self._process_file(ref_path)
        
        # Find :ref: references
        ref_pattern = re.compile(r':ref:`([^`]+)`')
        for match in ref_pattern.finditer(content):
            ref_name = match.group(1)
            ref_file = self._find_ref_file(ref_name)
            if ref_file:
                if "index" not in ref_file.name:
                    self._add_to_processed(ref_file)
                else:
                    self._process_file(ref_file)
        
        # Find :doc: references
        doc_pattern = re.compile(r':doc:`([^`]+)`')
        for match in doc_pattern.finditer(content):
            doc_path = match.group(1).split('<')[-1].split('>')[0]
            ref_path = self._resolve_path(file_path.parent, doc_path)
            if ref_path:
                self._process_file(ref_path)
    
    def _process_md_file(self, file_path: Path, content: str):
        """Process Markdown file for dependencies."""
        # Find markdown links
        md_link_pattern = r'\[.*?\]\((.*?)(?:\s.*?)?\)'
        for match in re.finditer(md_link_pattern, content):
            link = match.group(1).strip()
            if not link.startswith(('http://', 'https://', '#')):
                link_path = link.split('#')[0]
                ref_path = self._resolve_path(file_path.parent, link_path)
                if ref_path:
                    self._process_file(ref_path)
        
        # Find include directives
        md_include_pattern = r'\{include\}(\s*.*)'
        for match in re.finditer(md_include_pattern, content):
            include_path = match.group(1).strip()
            ref_path = self._resolve_path(file_path.parent, include_path)
            if ref_path:
                self._process_file(ref_path)
    
    def _resolve_path(self, base_dir: Path, path: str) -> Optional[Path]:
        """Resolve a path relative to a base directory."""
        path_ext = os.path.splitext(path)[1]
        if path_ext not in ['.rst', '.md', '']:
            return None
        
        # Try with different extensions
        for ext in ['.rst', '.md', '']:
            full_path = (base_dir / f"{path}{ext}").resolve()
            if full_path.exists():
                return full_path
        
        # Try from SDK_BASE
        base_dir_alt = Path(str(base_dir).replace(
            str(self.sdk_base / "docs"), 
            str(self.sdk_base)
        ))
        for ext in ['.rst', '.md', '']:
            full_path = (base_dir_alt / f"{path}{ext}").resolve()
            if full_path.exists():
                return full_path
        
        # Try as absolute path from docs
        for ext in ['.rst', '.md', '']:
            full_path = (self.sdk_base / "docs" / f"{path.lstrip('/')}{ext}").resolve()
            if full_path.exists():
                return full_path
        
        # Try as absolute path from SDK_BASE
        for ext in ['.rst', '.md', '']:
            full_path = (self.sdk_base / f"{path.lstrip('/')}{ext}").resolve()
            if full_path.exists():
                return full_path
        
        logger.debug(f"Could not resolve: {path} from {base_dir}")
        return None
    
    def _find_ref_file(self, ref_name: str) -> Optional[Path]:
        """Find the file that defines a reference."""
        for rst_file in self.sdk_base.glob('**/*.rst'):
            try:
                with open(rst_file, 'r', encoding='utf-8') as f:
                    if f".. _{ref_name}:" in f.read():
                        return rst_file
            except Exception:
                pass
        return None
    
    def _match_files_to_modules(self, config: dict) -> Set[str]:
        """Match included files to modules."""
        included_modules = set()
        
        for module_name, module_config in config.get('modules', {}).items():
            if 'external_contents' not in module_config:
                continue
            
            for content_config in module_config['external_contents']:
                pattern = content_config.get('pattern', '')
                
                for file_path in self.included_files:
                    normalized_path = os.path.normpath(file_path)
                    normalized_pattern = os.path.normpath(pattern)
                    
                    if fnmatch.fnmatch(normalized_path, normalized_pattern):
                        included_modules.add(module_name)
                        logger.debug(f"Matched {file_path} to {module_name}")
                        break
        
        return included_modules
