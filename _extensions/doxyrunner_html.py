"""
Doxyrunner HTML Mode Extension
##############################

This extension runs Doxygen to generate HTML documentation directly,
without XML intermediate format. This is more memory efficient for
large projects.
"""

import os
import shutil
import tempfile
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
from typing import Dict, Optional, Any
import re

from sphinx.application import Sphinx
from sphinx.util import logging

__version__ = "0.1.0"

logger = logging.getLogger(__name__)

def run_doxygen_html(doxygen: str, doxyfile_content: str) -> None:
    """Run Doxygen to generate HTML documentation."""
    
    f_doxyfile = tempfile.NamedTemporaryFile("w", delete=False)
    f_doxyfile.write(doxyfile_content)
    f_doxyfile.close()

    logger.info("Running Doxygen for HTML generation...")
    p = Popen([doxygen, f_doxyfile.name], stdout=PIPE, stderr=STDOUT, encoding="utf-8")
    
    while True:
        line = p.stdout.readline()
        if line:
            logger.debug(line.rstrip())
        if p.poll() is not None:
            break

    Path(f_doxyfile.name).unlink()

    if p.returncode:
        raise IOError(f"Doxygen process returned non-zero ({p.returncode})")

def process_doxyfile_html(
        doxyfile_path: str, 
        outdir: Path,
        fmt: bool = False,
        fmt_pattern: Optional[str] = None,
        fmt_vars: Optional[Dict[str, str]] = None,
        outdir_var: Path =None) -> str:
    """Process Doxyfile for HTML generation."""
    
    with open(doxyfile_path, encoding='utf-8') as f:
        content = f.read()
    
    # Ensure HTML generation is enabled
    content = content.replace("GENERATE_HTML          = NO", "GENERATE_HTML          = YES")
    if "GENERATE_HTML" not in content:
        content += "\nGENERATE_HTML          = YES\n"
    
    # Disable XML generation to save memory
    content = content.replace("GENERATE_XML           = YES", "GENERATE_XML           = NO")
    if "GENERATE_XML" not in content:
        content += "\nGENERATE_XML           = NO\n"
    
    # # Set output directory
    # content += f"\nOUTPUT_DIRECTORY       = {outdir_var.as_posix()}\n"
    content += f"\nHTML_OUTPUT            = html\n"
    
    # Optimize for memory usage
    content += "\nOPTIMIZE_OUTPUT_FOR_C  = YES\n"
    content += "\nEXTRACT_ALL            = NO\n"
    content += "\nEXTRACT_PRIVATE        = NO\n"
    content += "\nEXTRACT_STATIC         = NO\n"

    content = re.sub(
        r"^\s*OUTPUT_DIRECTORY\s*=.*$",
        f"OUTPUT_DIRECTORY={outdir.as_posix()}",
        content,
        flags=re.MULTILINE,
    )

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

def parse_device_info_from_project_name(project_name: str) -> Dict[str, str]:
    """Parse device information from project name.
    
    Expected format: drivers_{device_series}_{device_family}_{device_part}
    Example: drivers_MCX_MCXA_MCXA153 -> series=MCX, family=MCXA, part=MCXA153
    """
    parts = project_name.split('_')
    
    if len(parts) >= 4 and parts[0] == 'drivers':
        return {
            'series': parts[1],      # MCX
            'family': parts[2],      # MCXA  
            'part': parts[3],        # MCXA153
            'device_name': parts[3]  # MCXA153
        }
    else:
        # Fallback for non-standard naming
        device_name = parts[-1] if parts else project_name
        return {
            'series': 'Unknown',
            'family': 'Unknown',
            'part': device_name,
            'device_name': device_name
        }

def create_driver_index_html(project_name: str, outdir: Path, app: Sphinx) -> None:
    """Create driver index page that links directly to Doxygen HTML."""
    
    logger.info(f"Creating driver index for {project_name}")
    
    target_dir = str(outdir).replace("doxygen", "src")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Copy HTML documentation to the API directory structure
    html_source_dir = outdir / "html"
    api_target_dir = Path(app.outdir) / "api" / "drivers" / project_name
    api_target_dir.mkdir(parents=True, exist_ok=True)
    
    if html_source_dir.exists():
        try:
            # Copy HTML files to the API directory
            shutil.copytree(html_source_dir, api_target_dir, dirs_exist_ok=True)
            logger.info(f"HTML documentation copied to {api_target_dir}")
            
            # Calculate relative path from the RST file to the HTML index
            # RST file will be at: _build/src/drivers/{series}/{family}/{part}/index.rst
            # HTML will be at: _build/html/api/drivers/{series}/{family}/{part}/index.html
            # Relative path: ../../../../api/drivers/{series}/{family}/{part}/index.html
            html_rel_path = f"../../../../api/drivers/{project_name}/index.html"
            
        except Exception as e:
            logger.error(f"Failed to copy HTML documentation: {e}")
            # Fallback to direct path to doxygen output
            html_rel_path = f"../../../doxygen/drivers/{project_name}/html/index.html"
    else:
        logger.warning(f"HTML source directory not found: {html_source_dir}")
        return
    
    device_name = project_name.split("_")[-1]
    # Create the RST content
    rst_content = f""".. _{device_name}_drivers:

{device_name}
{'=' * len(device_name)}

This section contains the API reference documentation for the {device_name} device drivers.

API Documentation
#################

The complete API reference documentation is available in HTML format:

.. raw:: html

   <div style="margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
   <h4>📖 {device_name} API Reference</h4>
   <p>Click the button below to open the complete API documentation:</p>
   <p><a href="{html_rel_path}" target="_blank" style="background-color: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px; display: inline-block; margin-top: 10px;">Open API Documentation</a></p>
   </div>

Direct Link
###########

You can also access the API documentation directly: `{device_name} API Reference <{html_rel_path}>`__

"""
    
    # Write the index.rst file
    target_path = Path(target_dir) / "index.rst"
    with open(target_path, mode="w", encoding="utf-8") as f:
        f.write(rst_content)
    
    logger.info(f"Created driver index at {target_path}")
    logger.info(f"HTML documentation accessible at: {html_rel_path}")

def doxygen_html_build(app: Sphinx) -> None:
    """Main entry point for HTML mode Doxygen build."""
    
    if not hasattr(app.config, 'doxyrunner_html_doxydicts'):
        logger.warning("No doxyrunner_html_doxydicts configuration found")
        return
    
    doxygen_exe = getattr(app.config, 'doxyrunner_html_doxygen', 'doxygen')
    doxy_projects = app.config.doxyrunner_html_doxydicts
    
    logger.info(f"HTML Mode: Processing {len(doxy_projects)} Doxygen projects")
    
    for project_name, project_config in doxy_projects.items():
        logger.info(f"Processing HTML documentation for: {project_name}")
        
        doxyfile_path = project_config['doxyfile']
        outdir = Path(project_config['outdir'])
        
        # Create output directory
        outdir.mkdir(parents=True, exist_ok=True)
        
        # Process Doxyfile for HTML generation
        doxyfile_content = process_doxyfile_html(
            doxyfile_path, 
            outdir,
            app.config.doxyrunner_html_fmt,
            app.config.doxyrunner_html_fmt_pattern,
            app.config.doxyrunner_html_fmt_vars,
            app.config.doxyrunner_html_outdir_var)
        
        # Run Doxygen
        try:
            run_doxygen_html(doxygen_exe, doxyfile_content)
            logger.info(f"HTML documentation generated for {project_name}")
            
            # Create an index file that links to the HTML documentation
            html_dir  = outdir / "html" 
            if html_dir.exists():
                # # Copy to a location accessible by Sphinx
                # sphinx_html_dir = Path(app.outdir) / "api" / project_name
                # sphinx_html_dir.mkdir(parents=True, exist_ok=True)
                
                # # Copy the entire HTML directory
                # html_src = outdir / "html"
                # if html_src.exists():
                #     shutil.copytree(html_src, sphinx_html_dir, dirs_exist_ok=True)
                #     logger.info(f"HTML documentation copied to {sphinx_html_dir}")

                # Create driver index page for driver projects
                if project_name.startswith("drivers"):
                    create_driver_index_html(project_name, outdir, app)
            else:
                logger.warning(f"No HTML directory found at {html_dir}")
        except Exception as e:
            logger.error(f"Failed to generate HTML documentation for {project_name}: {e}")

def setup(app: Sphinx) -> Dict[str, Any]:
    """Setup the HTML mode extension."""
    
    app.add_config_value("doxyrunner_html_doxygen", "doxygen", "env")
    app.add_config_value("doxyrunner_html_doxydicts", {}, "env")
    app.add_config_value("doxyrunner_html_fmt", False, "env")
    app.add_config_value("doxyrunner_html_fmt_vars", {}, "env")
    app.add_config_value("doxyrunner_html_outdir_var", None, "env")
    app.add_config_value("doxyrunner_html_fmt_pattern", "@{}@", "env")
    app.add_config_value("doxyrunner_html_mode", 1, "")

    app.connect("builder-inited", doxygen_html_build)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
