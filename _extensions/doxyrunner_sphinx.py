"""
Copyright 2025-2026 NXP
SPDX-License-Identifier: BSD-3-Clause

Doxyrunner Sphinx Mode Extension
################################

This extension creates separate Sphinx projects for each device,
allowing for better organization and parallel processing.
"""

import os
import shutil
import tempfile
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
from typing import Dict, Any
import concurrent.futures
import collections
import re

from sphinx.application import Sphinx
from sphinx.util import logging
from jinja2 import Environment, FileSystemLoader

# Import XML parsing functionality from doxyrunner
try:
    import doxmlparser
    from doxmlparser.compound import DoxCompoundKind, DoxMemberKind
    HAS_DOXMLPARSER = True
except ImportError:
    HAS_DOXMLPARSER = False
    logger = logging.getLogger(__name__)
    logger.warning("doxmlparser not available, XML parsing will be limited")

__version__ = "0.1.0"

logger = logging.getLogger(__name__)

def run_doxygen_for_sphinx(doxygen: str, doxyfile_content: str) -> None:
    """Run Doxygen to generate XML for Sphinx."""
    
    f_doxyfile = tempfile.NamedTemporaryFile("w", delete=False, suffix=".doxyfile")
    f_doxyfile.write(doxyfile_content)
    f_doxyfile.close()

    logger.info("Running Doxygen for Sphinx XML generation...")
    logger.debug(f"Using Doxyfile: {f_doxyfile.name}")
    
    try:
        p = Popen([doxygen, f_doxyfile.name], stdout=PIPE, stderr=STDOUT, encoding="utf-8")
        
        output_lines = []
        while True:
            line = p.stdout.readline()
            if line:
                line = line.rstrip()
                output_lines.append(line)
                logger.debug(f"Doxygen: {line}")
            if p.poll() is not None:
                break

        if p.returncode != 0:
            logger.error(f"Doxygen failed with return code: {p.returncode}")
            logger.error("Doxygen output:")
            for line in output_lines:
                logger.error(f"  {line}")
            raise IOError(f"Doxygen process returned non-zero ({p.returncode})")
        else:
            logger.info("Doxygen completed successfully")
            
    except Exception as e:
        logger.error(f"Exception running Doxygen: {e}")
        raise
    finally:
        # Only delete the temp file if Doxygen succeeded
        if p.returncode == 0:
            try:
                Path(f_doxyfile.name).unlink()
            except:
                pass

def process_doxyfile_sphinx(doxyfile_path: str, outdir: Path, 
                          fmt: bool = False,
                          fmt_pattern: str = None,
                          fmt_vars: Dict[str, str] = None,
                          outdir_var: str = None) -> str:
    """Process Doxyfile for Sphinx XML generation.
    
    This function is based on process_doxyfile_html but configured for XML output.
    """
    
    logger.info(f"Processing Doxyfile for Sphinx: {doxyfile_path}")
    
    if not os.path.exists(doxyfile_path):
        raise FileNotFoundError(f"Doxyfile not found: {doxyfile_path}")
    
    with open(doxyfile_path, encoding='utf-8') as f:
        content = f.read()
    
    logger.debug(f"Original Doxyfile size: {len(content)} characters")
    
    # Ensure XML generation is enabled
    if "GENERATE_XML" in content:
        content = content.replace("GENERATE_XML           = NO", "GENERATE_XML           = YES")
        content = content.replace("GENERATE_XML = NO", "GENERATE_XML = YES")
    else:
        content += "\nGENERATE_XML           = YES\n"
    
    # Disable HTML generation to save memory
    if "GENERATE_HTML" in content:
        content = content.replace("GENERATE_HTML          = YES", "GENERATE_HTML          = NO")
        content = content.replace("GENERATE_HTML = YES", "GENERATE_HTML = NO")
    else:
        content += "\nGENERATE_HTML          = NO\n"
    
    # Set output directory
    outdir.mkdir(parents=True, exist_ok=True)
    
    # Use regex replacement similar to doxyrunner.py
    content = re.sub(
        r"^\s*OUTPUT_DIRECTORY\s*=.*$",
        f"OUTPUT_DIRECTORY={outdir.as_posix()}",
        content,
        flags=re.MULTILINE,
    )
    
    content += f"\nXML_OUTPUT             = xml\n"
    
    # Add warn format for better error reporting
    content = re.sub(
        r"^\s*WARN_FORMAT\s*=.*$",
        'WARN_FORMAT="$file:$line: $text"',
        content,
        flags=re.MULTILINE,
    )
    
    # Set quiet mode
    content = re.sub(
        r"^\s*QUIET\s*=.*$",
        "QUIET=NO",  # Enable output for debugging
        content,
        flags=re.MULTILINE,
    )
    
    # Optimize for memory usage
    content += "\nOPTIMIZE_OUTPUT_FOR_C  = YES\n"
    content += "\nEXTRACT_ALL            = NO\n"
    content += "\nEXTRACT_PRIVATE        = NO\n"
    content += "\nEXTRACT_STATIC         = NO\n"
    content += "\nWARNINGS               = YES\n"
    content += "\nWARN_IF_UNDOCUMENTED   = NO\n"
    
    # Apply format variables if provided (similar to doxyrunner.py)
    if fmt and fmt_pattern and fmt_vars:
        logger.debug(f"Applying format variables: {fmt_vars}")
        
        if outdir_var:
            fmt_vars = fmt_vars.copy()
            fmt_vars[outdir_var] = outdir.as_posix()
            logger.debug(f"Added outdir variable {outdir_var}: {outdir.as_posix()}")

        for var, value in fmt_vars.items():
            pattern = fmt_pattern.format(var)
            logger.debug(f"Replacing {pattern} with {value}")
            content = content.replace(pattern, str(value))
    
    logger.debug(f"Processed Doxyfile size: {len(content)} characters")
    
    return content

def get_group_names_from_xml(xml_dir: Path, compound_id: str) -> Dict[str, str]:
    """Get group names from XML compound file.
    
    Based on get_group_names function from doxyrunner.py
    """
    if not HAS_DOXMLPARSER:
        logger.warning("doxmlparser not available, cannot parse XML groups")
        return {}
    
    try:
        xml_file = xml_dir / f"{compound_id}.xml"
        if not xml_file.exists():
            return {}
        
        rootObj = doxmlparser.compound.parse(str(xml_file), True)
        group_names = {}

        for compounddef in rootObj.get_compounddef():
            name = compounddef.get_compoundname()
            if compounddef.get_kind() == DoxCompoundKind.GROUP:
                group_names[name] = compounddef.get_title()

        return group_names
    except Exception as e:
        logger.error(f"Error parsing XML file {xml_file}: {e}")
        return {}

def parse_generated_xml_index(xml_dir: Path) -> Dict[str, str]:
    """Parse generated XML index to extract group information.
    
    Based on parse_generated_index function from doxyrunner.py
    """
    if not HAS_DOXMLPARSER:
        logger.warning("doxmlparser not available, using fallback group parsing")
        return {"api": "API Reference"}
    
    try:
        index_file = xml_dir / "index.xml"
        if not index_file.exists():
            logger.warning(f"XML index file not found: {index_file}")
            return {"api": "API Reference"}
        
        rootObj = doxmlparser.index.parse(str(index_file), True)
        compounds = rootObj.get_compound()
        group_names = {}

        # Use concurrent processing like in doxyrunner.py
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [
                executor.submit(get_group_names_from_xml, xml_dir, compound.get_refid())
                for compound in compounds
            ]
            for future in concurrent.futures.as_completed(futures):
                page_group_names = future.result()
                group_names.update(page_group_names)

        logger.info(f"Parsed {len(group_names)} groups from XML")
        return group_names if group_names else {"api": "API Reference"}
        
    except Exception as e:
        logger.error(f"Error parsing XML index: {e}")
        return {"api": "API Reference"}

def create_device_sphinx_project(project_name: str, project_config: dict, base_dir: Path, xml_dir: Path) -> None:
    """Create a separate Sphinx project for a device.
    
    Based on create_driver_tree function from doxyrunner.py but creates a full Sphinx project.
    """
    
    device_name = project_name.split('_')[-1] if '_' in project_name else project_name
    project_dir = base_dir / f"device_{device_name}"
    project_dir.mkdir(parents=True, exist_ok=True)
    sdk_version = project_config.get('version', '1.0.0')
    
    logger.info(f"Creating Sphinx project for {device_name} at {project_dir}")
    
    # Parse group names from XML (similar to create_driver_tree)
    group_names = parse_generated_xml_index(xml_dir)
    
    # Create conf.py for the device project
    conf_content = f'''# Device-specific Sphinx configuration for {device_name}
import os
import sys

project = 'MCUXpresso SDK - {device_name} API Reference'
copyright = '2025, NXP'
author = 'NXP'
version = '{sdk_version}'

extensions = [
    'breathe',
    'sphinx_book_theme',
]

if os.path.exists(os.path.join(os.path.dirname(__file__), '../../../internal/images/nxp_logo_small.png')):
    html_logo = "../../../internal/images/nxp_logo_small.png"

breathe_projects = {{
    "{device_name}": "_doxygen/xml"
}}
breathe_default_project = "{device_name}"
breathe_separate_member_pages = True

breathe_domain_by_extension = {{
    "h": "c",
    "c": "c",
}}

html_theme = 'sphinx_book_theme'
html_title = f'{{project}}'


html_theme_options = {{
    "logo": {{
        "text": f"{{project}} v{{version}}",
    }},
}}

master_doc = 'index'
'''
    
    with open(project_dir / "conf.py", "w") as f:
        f.write(conf_content)
    
    # Create index.rst using template approach from doxyrunner.py
    create_device_index_rst(project_dir, device_name, project_name, group_names)
    
    logger.info(f"Created Sphinx project for {device_name}")

def create_device_index_rst(project_dir: Path, device_name: str, project_name: str, group_names: Dict[str, str]) -> None:
    """Create device index RST file using template approach.
    
    Based on create_driver_tree function from doxyrunner.py
    """
    
    # Try to use the same template approach as doxyrunner.py
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template/")
    
    if os.path.exists(template_dir):
        try:
            logger.info(f'Using template directory: {template_dir}')
            environment = Environment(loader=FileSystemLoader(template_dir))
            template = environment.get_template("device_rm.tmp")
            
            parameters = {
                "device_name": device_name, 
                "group_names": collections.OrderedDict(sorted(group_names.items())), 
                "prj_name": device_name
            }

            content = template.render(parameters=parameters)
            
        except Exception as e:
            logger.warning(f"Failed to use template: {e}, falling back to manual generation")
            content = create_manual_device_index(device_name, project_name, group_names)
    else:
        logger.warning(f"Template directory not found: {template_dir}, using manual generation")
        content = create_manual_device_index(device_name, project_name, group_names)
    
    # Write the index.rst file
    target_path = project_dir / "index.rst"
    with open(target_path, mode="w", encoding="utf-8") as f:
        f.write(content)
    
    logger.info(f"Created device index at {target_path}")

def create_manual_device_index(device_name: str, project_name: str, group_names: Dict[str, str]) -> str:
    """Create device index content manually if template is not available."""
    
    content = f""".. _{device_name}_drivers:

{device_name}
{'=' * len(device_name)}

This section contains the API reference documentation for the {device_name} device drivers.

"""

    if group_names:
        for group_id, group_title in sorted(group_names.items()):
            content += f"""
{group_title}
{'#' * len(group_title)}

.. doxygengroup:: {group_id}
    :project: {project_name}
    :content-only:
    :members:
    :no-link:

"""
    else:
        content += """
API Reference
#############

.. doxygenindex::
   :project: {project_name}

"""
    
    return content

def create_driver_index_sphinx(project_name: str, outdir: Path, app: Sphinx) -> None:
    """Create driver index page that references the intersphinx device project.
    
    Similar to create_driver_index_html but creates references to Sphinx projects.
    """
    
    logger.info(f"Creating driver index for {project_name}")
    
    # Parse device information
    device_name = project_name.split("_")[-1]
    html_rel_path = f"../../../../api/devices/{device_name}/index.html"
    
    logger.info(f"Device info: {device_name}")
    
    # Create target directory in the source tree
    target_dir = Path(str(outdir).replace("doxygen","src"))
    logger.info(f"target dir: {target_dir}")
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the RST content with direct HTML references
    rst_content = f""".. _{device_name}_drivers:

{device_name}
{'=' * len(device_name)}

This section contains the API reference documentation for the {device_name} device drivers.

API Documentation
#################

You can access the API documentation directly: `{device_name} API Reference <{html_rel_path}>`__

"""
    
    # Write the index.rst file
    target_path = target_dir / "index.rst"
    with open(target_path, mode="w", encoding="utf-8") as f:
        f.write(rst_content)
    
    logger.info(f"Created driver index at {target_path}")
    logger.info(f"Device documentation accessible at: api/devices/{device_name}/")


def copy_device_html_to_main_build(device_projects: list, main_html_dir: Path) -> None:
    """Copy device project HTML to main build directory.
    
    IMPROVEMENT 1: Copy device HTML to main _build/html folder for html references.
    """
    
    logger.info("Copying device project HTML to main build directory...")
    
    # Create api/devices directory in main HTML output
    devices_api_dir = main_html_dir / "api" / "devices"
    devices_api_dir.mkdir(parents=True, exist_ok=True)
    
    for project_dir in device_projects:
        device_name = project_dir.name.replace("device_", "")
        device_html_src = project_dir / "_build" / "html"
        device_html_dest = devices_api_dir / device_name
        
        if device_html_src.exists():
            try:
                # Remove existing destination if it exists
                if device_html_dest.exists():
                    shutil.rmtree(device_html_dest)
                
                # Copy the HTML documentation
                shutil.copytree(device_html_src, device_html_dest)
                logger.info(f"Copied {device_name} HTML to {device_html_dest}")
                
            except Exception as e:
                logger.error(f"Failed to copy HTML for {device_name}: {e}")
        else:
            logger.warning(f"HTML source not found for {device_name}: {device_html_src}")

def build_device_project(project_dir: Path) -> bool:
    """Build a device Sphinx project."""
    
    try:
        logger.info(f"Building Sphinx project: {project_dir}")
        
        # Run sphinx-build
        cmd = [
            "sphinx-build",
            "-b", "html",
            "--keep-going", "-T",
            str(project_dir),
            str(project_dir / "_build" / "html")
        ]
        
        p = Popen(cmd, stdout=PIPE, stderr=STDOUT, encoding="utf-8")
        
        while True:
            line = p.stdout.readline()
            if line:
                logger.debug(f"[{project_dir.name}] {line.rstrip()}")
            if p.poll() is not None:
                break
        
        if p.returncode == 0:
            logger.info(f"Successfully built {project_dir.name}")
            return True
        else:
            logger.error(f"Failed to build {project_dir.name} (exit code: {p.returncode})")
            return False
            
    except Exception as e:
        logger.error(f"Exception building {project_dir.name}: {e}")
        return False

def doxygen_sphinx_build(app: Sphinx) -> None:
    """Main entry point for Sphinx mode Doxygen build."""
    
    # Check if Sphinx mode is enabled
    if not getattr(app.config, 'doxyrunner_sphinx_mode', 0):
        logger.info("Sphinx mode disabled, skipping doxyrunner_sphinx")
        return
    
    if not hasattr(app.config, 'doxyrunner_sphinx_doxydicts'):
        logger.warning("No doxyrunner_sphinx_doxydicts configuration found")
        return
    
    doxygen_exe =app.config.doxyrunner_sphinx_doxygen
    doxy_projects = app.config.doxyrunner_sphinx_doxydicts
    
    logger.info(f"Sphinx Mode: Processing {len(doxy_projects)} Doxygen projects")
    
    # Check if Doxygen is available
    try:
        test_p = Popen([doxygen_exe, '--version'], stdout=PIPE, stderr=PIPE, encoding="utf-8")
        stdout, stderr = test_p.communicate()
        if test_p.returncode == 0:
            logger.info(f"Doxygen version: {stdout.strip()}")
        else:
            logger.error(f"Doxygen test failed: {stderr}")
            return
    except Exception as e:
        logger.error(f"Cannot run Doxygen: {e}")
        return
    
    # Create base directory for device projects
    base_dir = Path(app.srcdir).parent / "device_projects"
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # Process each Doxygen project
    device_projects = []
    
    for project_name, project_config in doxy_projects.items():
        logger.info(f"Processing Sphinx documentation for: {project_name}")
        
        doxyfile_path = project_config['doxyfile']
        outdir = Path(project_config['outdir'])
        project_config['version'] = project_config.get('version',str(app.config.version))
        
        # Create output directory
        doxy_outdir = outdir / "_doxygen"
        doxy_outdir.mkdir(parents=True, exist_ok=True)
        
        # Process Doxyfile for XML generation (using the updated function)
        try:
            doxyfile_content = process_doxyfile_sphinx(
                doxyfile_path, 
                doxy_outdir,
                app.config.doxyrunner_sphinx_fmt,
                app.config.doxyrunner_sphinx_fmt_pattern,
                app.config.doxyrunner_sphinx_fmt_vars,
                app.config.doxyrunner_sphinx_outdir_var
            )
        except Exception as e:
            logger.error(f"Failed to process Doxyfile {doxyfile_path}: {e}")
            continue
        
        # Run Doxygen
        try:
            run_doxygen_for_sphinx(doxygen_exe, doxyfile_content)
            logger.info(f"XML documentation generated for {project_name}")
            
            xml_dir = doxy_outdir / "xml"
            if xml_dir.exists():
                # Create Sphinx project for this device (using updated function)
                create_device_sphinx_project(project_name, project_config, base_dir, xml_dir)
                
                # Copy XML files to device project
                device_name = project_name.split('_')[-1] if '_' in project_name else project_name
                device_project_dir = base_dir / f"device_{device_name}"
                device_doxy_dir = device_project_dir / "_doxygen"
                
                shutil.copytree(xml_dir, device_doxy_dir / "xml", dirs_exist_ok=True)
                device_projects.append(device_project_dir)
                # NEW: Create device driver index files
                if project_name.startswith("drivers"):
                    create_driver_index_sphinx(project_name, outdir, app)
            else:
                logger.warning(f"No XML directory found at {xml_dir}")
                
        except Exception as e:
            logger.error(f"Failed to generate XML documentation for {project_name}: {e}")
    
    # Build all device projects in parallel
    if device_projects:
        logger.info(f"Building {len(device_projects)} device Sphinx projects...")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(build_device_project, proj_dir) for proj_dir in device_projects]
            
            results = []
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
        
        successful_builds = sum(results)
        logger.info(f"Successfully built {successful_builds}/{len(device_projects)} device projects")
        # IMPROVEMENT 1: Copy device HTML to main build directory
        main_html_dir = Path(app.outdir)
        copy_device_html_to_main_build(device_projects, main_html_dir)

def setup(app: Sphinx) -> Dict[str, Any]:
    """Setup the Sphinx mode extension."""

    app.add_config_value("doxyrunner_sphinx_doxygen", "doxygen", "env")
    app.add_config_value("doxyrunner_sphinx_doxydicts", {}, "env")
    app.add_config_value("doxyrunner_sphinx_fmt", False, "env")
    app.add_config_value("doxyrunner_sphinx_fmt_vars", {}, "env")
    app.add_config_value("doxyrunner_sphinx_outdir_var", None, "env")
    app.add_config_value("doxyrunner_sphinx_fmt_pattern", "@{}@", "env")
    app.add_config_value("doxyrunner_sphinx_mode", 1, "")
    app.connect("builder-inited", doxygen_sphinx_build)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
