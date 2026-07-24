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

# Patch documents not included in any toctree to suppress orphan warnings.
# These are legitimate standalone documents (readmes, changelogs, known issues,
# shared readmes, etc.) that are included via `{include}` directives or are
# auxiliary files copied by external_content but not directly in a toctree.
_ORPHAN_PATTERNS = (
    # Board getting-started topics (gsindex.md hidden toctree: topics/*)
    'gettingStarted/',
    # Board release notes
    'releaseNotes/',
    # Examples: card-driven navigation (examples_catalog) — the examples
    # index carries no toctree, so every example doc is a legitimate
    # standalone page reached from the catalog cards.
    'examples/',
    'example_board_readme',
    'examples_shared_readme',
    'board_readme',
    'readme_modules',
    # Bifrost docs linked from bifrost/readme.md but not in a toctree
    'bifrost/docs/',
    # Files linked from READMEs/release notes but not in any toctree
    'mcmgr/tests/test_heartbeat/',
    'mcmgr/doxygen/porting_guide',
    'freertos-kernel/CHANGELOG',
    'executorch/docs/source/',
    'lvgl/docs/src/details/debugging/',
    # Examples: display/lvgl readmes
    'lvgl_examples_readme',
    'lcdif_examples_readme',
    'lcdifv2_examples_readme',
    'dcif_examples_readme',
    'jpegdec_examples_readme',
    # Examples: ecat topics (shared across ecat_examples)
    'ecat_examples/topics/',
    # Examples: other standalone docs
    'examples/ncp_examples/',
    'examples/ota_examples/',
    'wifi_examples/common/',
    # ChangeLog / CHANGELOG files (drivers, examples, boards)
    'ChangeLog_',
    'ChangeLog',
    'CHANGELOG',
    # Release: known_issues, commonrn
    'release/known_issues/',
    'commonrn',
    # FreeRTOS: coremqtt-agent README
    'rtos/freertos/coremqtt-agent/README',
    # GSD common docs
    'gsd/package',
    'gsd/repo',
    # Standalone middleware/firmware docs referenced from example readmes
    'middleware/eiq/mpp/Build',
    'firmware/edgelock/',
    # Upstream TF-M excludes this key readme from its own build
    'platform/cypress/psoc64/security/keys/readme',
    # Wi-Fi API reference is linked (not toctree'd) from the wifi docs index
    'middleware/wifi_nxp/docs/freertos/',
    # --- MCUX-88966: remaining toctree-orphan sweep (2026-07 build) ---
    # RT700 Xplorer getting-started topics (parallel of 'gettingStarted/';
    # the Xplorer variant directory name does not match that pattern)
    'gettingStartedXplorer/',
    # Docs-repo standalone engineering notes linked from other guides
    'develop/build_system/Best_Practice',
    'develop/sdk/internal_example_device_board_definition',
    # Edgefast user-guide trees copied by external_content, reached by links
    'middleware/edgefast_open/docs/',
    # eiq executorch NXP readme (source/ tree already covered above)
    'executorch/docs/nxp/README',
    # littlefs vendored auxiliary docs (README stays toctree'd)
    'littlefs/DESIGN',
    'littlefs/LICENSE',
    'littlefs/SPEC',
    # mcu_bootloader per-device flashloader / manufacturing guides
    'iMXRT1050_Manufacturing_User_Guide/topics/',
    'LPC540XX_Flashloader_Release_Notes/topics/',
    'iMXRT1160_Flashloader_Release_Notes/',
    # mcuboot / multicore vendored auxiliary docs
    'mcuboot_opensource/CODE_OF_CONDUCT',
    'middleware/multicore/README',
    'erpc/CONTRIBUTING',
    'erpc/doxygen/mainpage_',
    'eRPC_GettingStarted/',
    'rpmsg-lite/doxygen/',
    # safety zephyr readmes (upstream-shipped)
    'middleware/safety_iec60730b/zephyr/',
    # vglite standalone topics linked from the vglite guide
    'middleware/vglite/topics/',
    # WiFi-BT-802.15.4 certification/legal topics reached via deep links
    'middleware/wireless/WiFi-Bluetooth-802.15.4/topics/',
    # BLE demo guide topic included via {include}
    'Bluetooth Low Energy Demo Applications Users Guide/topics/switches_and_pins',
    # Connectivity framework service readmes linked from the framework index
    'framework/services/DBG/',
    'framework/services/WorkQ/',
    # 802.15.4 connectivity-test guide legal page
    'connectivity_test/UG10204/topics/',
)

def patch_orphan_docs(app, docname, source):
    if not any(pattern in docname for pattern in _ORPHAN_PATTERNS):
        return

    content = source[0]
    is_markdown = str(app.env.doc2path(docname)).endswith('.md')

    if is_markdown:
        if content.lstrip().startswith('---'):
            # Has existing frontmatter — insert orphan into it
            stripped = content.lstrip()
            end = stripped.find('---', 3)
            if end != -1 and 'orphan' not in stripped[:end]:
                source[0] = content[:len(content)-len(stripped)] + '---\norphan: true\n' + stripped[3:]
        else:
            # No frontmatter — add one
            source[0] = '---\norphan: true\n---\n\n' + content
    else:
        # RST files
        if ':orphan:' not in content:
            source[0] = ':orphan:\n\n' + content


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

def validate_html_paths(app, exception):
    """
    Validate that HTML output paths don't contain prohibited characters.
    Called after build is complete.
    """
    if exception is not None:
        return

    from pathlib import Path
    import re

    # Prohibited characters according to IT security policy
    PROHIBITED_CHARS = r'[$%();<>?\[\]`{|}]'

    outdir = Path(app.outdir)
    if not outdir.exists():
        return

    violations = []

    # Check all HTML files and their paths
    for html_file in outdir.rglob('*.html'):
        rel_path = html_file.relative_to(outdir)
        path_str = str(rel_path)

        # Check for prohibited characters in the path
        matches = re.findall(PROHIBITED_CHARS, path_str)
        if matches:
            violations.append({
                'path': path_str,
                'chars': set(matches)
            })

    # Report violations
    if violations:
        logger.error("=" * 80)
        logger.error("SECURITY POLICY VIOLATION: Prohibited characters found in HTML paths")
        logger.error("=" * 80)
        logger.error("The following paths contain prohibited characters: \"$%();<>?[]`{|}")
        logger.error("")

        for v in violations:
            logger.error(f"Path: {v['path']}")
            logger.error(f"  Prohibited characters found: {', '.join(sorted(v['chars']))}")
            logger.error("")

        logger.error("=" * 80)
        logger.error("Please rename files/directories to remove these characters")
        logger.error("=" * 80)

        # Make the build fail
        raise Exception("Build failed: HTML paths contain prohibited characters")
    else:
        logger.info("Path validation: No prohibited characters found in HTML output paths")

class _CDomainParseErrorFilter:
    """Filter out C domain parse errors from breathe/doxygen-generated declarations.

    These warnings are caused by complex C macros, function pointers, and
    non-standard syntax in doxygen XML that the Sphinx C domain parser cannot
    handle.  They are not actionable without modifying upstream headers.
    """
    _SUPPRESSED = (
        'Invalid C declaration',
        'Error in declarator',
    )

    def filter(self, record):
        msg = record.getMessage() if hasattr(record, 'getMessage') else str(record.msg)
        return not any(p in msg for p in self._SUPPRESSED)

class _ThirdPartyDocWarningFilter:
    """Drop warnings that originate from unmodifiable third-party documents.

    The paths below hold upstream documentation shipped verbatim (e.g. the
    Mbed TLS design documents under middleware/mbedtls3x/docs).  Their
    cross-references target the upstream project's own doc layout and cannot
    be fixed without diverging from upstream, so warnings raised from these
    sources are not actionable in this repository.
    """
    _PATHS = (
        'middleware/mbedtls3x/docs/',
        # ARM upstream psa-arch-tests tree: its READMEs link files/dirs that
        # are not part of the SDK docs build (owned/fixed upstream)
        'middleware/tfm/psa-arch-tests/',
        # TF-M cross-project references (resolved via intersphinx in the
        # upstream multi-project doc build; those projects are not part of
        # the SDK docs)
        "'TF-M-Tests:",
        "'TF-M-Tools:",
        "'TF-M-Extras:",
        # TF-M's own cross-project doc references (same class as above:
        # resolved by intersphinx in the upstream multi-project build)
        "'TF-M:",
        # littlefs is a vendored upstream tree; its README links repo files
        # (bd/lfs_testbd.h) that no longer exist at the vendored revision and
        # SPEC/DESIGN carry upstream-style transitions - fixed upstream only.
        'middleware/littlefs/',
    )

    def filter(self, record):
        import logging
        if record.levelno < logging.WARNING:
            return True
        location = str(getattr(record, 'location', '') or '').replace('\\', '/')
        msg = record.getMessage() if hasattr(record, 'getMessage') else str(record.msg)
        msg = msg.replace('\\', '/')
        return not any(p in location or p in msg for p in self._PATHS)

def _install_third_party_warning_filter(app):
    # Attach at handler level of the root "sphinx" logger so warnings from
    # every sphinx.* child logger (myst xrefs, images, toctree, std domain)
    # are filtered regardless of which module emits them.
    import logging
    tp_filter = _ThirdPartyDocWarningFilter()
    for handler in logging.getLogger('sphinx').handlers:
        handler.addFilter(tp_filter)

# Standalone third-party doc trees whose doc-root-absolute references are
# re-based by the subtree_docroot extension.
subtree_docroots = [
    'middleware/tfm/tf-m/docs',
]

# Doc trees whose raw-HTML anchors (<a name=...> in table cells, emitted by
# Doxygen/DITA conversion) are registered as link targets (html_anchors ext).
html_anchor_docroots = [
    'middleware/eiq',
    'middleware/wifi_nxp/docs',
    'examples/_boards',
    'middleware/edgefast_open/docs',
    'middleware/mcu_bootloader/docs',
    'boards/',
    'middleware/wireless/bluetooth/doc',
    'middleware/wireless/WiFi-Bluetooth-802.15.4',
]

# Source files exposed as syntax-highlighted viewer pages (source_pages ext).
# Workspace-relative paths; links to these files from any document are
# transparently redirected to the generated pages under _sources_view/.
source_pages_files = [
    # EdgeLock 2GO agent configuration headers and referenced sources
    'middleware/nxp_iot_agent/inc/nxp_iot_agent_config.h',
    'middleware/nxp_iot_agent/inc/nxp_iot_agent_config_credentials.h',
    'middleware/nxp_iot_agent/ex/inc/iot_agent_demo_config.h',
    'middleware/nxp_iot_agent/ex/src/network/iot_agent_network_lwip_wifi.c',
    'middleware/nxp_iot_agent/ex/src/utils/iot_agent_claimcode_inject.c',
    'middleware/nxp_iot_agent/ex/src/apps/el2go_claimcode_encryption.c',
    'middleware/nxp_iot_agent/ex/src/apps/psa_examples/el2go_csr/pal/el2go_csr_console.h',
    'middleware/nxp_iot_agent/tst/el2go_blob_test/scripts/requirements.txt',
    # TF-M platform files referenced by el2go TrustZone examples
    'middleware/tfm/tf-m/platform/ext/target/nxp/frdmrw612/config_tfm_target.h',
    'middleware/tfm/tf-m/platform/ext/target/nxp/frdmrw612/partition/flash_layout.h',
    'middleware/tfm/tf-m/platform/ext/target/nxp/frdmrw612/partition/region_defs.h',
    # Components referenced by example readmes
    'components/conn_fwloader/readme.txt',
    'components/debug/coredump/scripts/coredump_gdbserver.py',
    # Connectivity framework SecLib flavors and configuration
    'middleware/wireless/framework/services/SecLib_RNG/SecLib.c',
    'middleware/wireless/framework/services/SecLib_RNG/SecLib_sss.c',
    'middleware/wireless/framework/services/SecLib_RNG/SecLib_psa.c',
    'middleware/wireless/framework/services/SecLib_RNG/RNG.c',
    'middleware/wireless/framework/services/SecLib_RNG/RNG_psa.c',
    'middleware/wireless/framework/services/SecLib_RNG/CMakeLists.txt',
    'middleware/wireless/framework/services/SecLib_RNG/Kconfig',
    'middleware/wireless/framework/platform/wireless_mcu/configs/SecLib_psa_config.h',
    # RT700 TrustZone example support files
    'examples/_boards/mimxrt700evk/trustzone_examples/linkscripts/MIMXRT798Sxxxx_cm33_core0_flash_s.icf',
    'examples/_boards/mimxrt700evk/trustzone_examples/linkscripts/MIMXRT798Sxxxx_cm33_core0_flash_ns.icf',
    'examples/_boards/mimxrt700evk/trustzone_examples/hello_world/hello_world_s/cm33_core0/tzm_config.c',
    'examples/_boards/mimxrt700evk/trustzone_examples/hello_world/hello_world_s/cm33_core0/reconfig.cmake',
    'examples/_boards/mimxrt700evk/trustzone_examples/secure_gpio/secure_gpio_s/cm33_core0/tzm_config.c',
    'examples/_boards/mimxrt700evk/trustzone_examples/secure_gpio/secure_gpio_s/cm33_core0/reconfig.cmake',
    'examples/_boards/mimxrt700evk/trustzone_examples/secure_faults/secure_faults_s/cm33_core0/tzm_config.c',
    'examples/_boards/mimxrt700evk/trustzone_examples/secure_faults/secure_faults_s/cm33_core0/reconfig.cmake',
    'examples/_boards/mimxrt700evk/trustzone_examples/secure_gpio/secure_gpio_s/cm33_core0/tzm_config.c',
    'examples/_boards/mimxrt700evk/trustzone_examples/secure_gpio/secure_gpio_s/cm33_core0/reconfig.cmake',
    # SDK generator data schemas
    'ecosystem/sdk_generator/lib/argparser/schemas/config_file_schema.json',
    'ecosystem/sdk_generator/data/sdk_data_schema/v3/component_schema.json',
    'ecosystem/sdk_generator/data/sdk_data_schema/v3/container_schema.json',
    'ecosystem/sdk_generator/data/sdk_data_schema/v3/project_segment_schema.json',
    'ecosystem/sdk_generator/data/sdk_data_schema/v3/project_schema.json',
    'ecosystem/sdk_generator/data/sdk_data_schema/v3/license_schema.json',
]

def setup(app):
    app.connect('source-read', patch_orphan_docs)
    app.connect('source-read', patch_mcuboot_readme)
    app.connect('build-finished', validate_html_paths)
    app.connect('builder-inited', _install_third_party_warning_filter)

    # Suppress C domain parse errors from breathe/doxygen
    import logging
    logging.getLogger('sphinx.domains.c').addFilter(_CDomainParseErrorFilter())

    # Lexer aliases for code-fence languages Pygments doesn't know
    # ("Pygments lexer name 'X' is not known" warnings). Registering aliases
    # here resolves every occurrence build-wide without editing fences across
    # owner repos, where vendored trees would regress on the next sync.
    from pygments.lexers.shell import BashLexer, BatchLexer
    from pygments.lexers.special import TextLexer
    app.add_lexer('commandline', BashLexer)  # eiq/executorch shell commands
    app.add_lexer('cmd', BatchLexer)         # bifrost Windows commands
    app.add_lexer('txt', TextLexer)          # common alias authors reach for; Pygments only knows 'text'
    app.add_lexer('ld', TextLexer)           # linker scripts (no Pygments lexer exists)
    app.add_lexer('mermaid', TextLexer)      # PDF-build fallback: HTML builds render
                                             # diagrams via sphinxmermaid + fence-as-
                                             # directive (see extensions setup above)
    app.add_lexer('Lowpower', TextLexer)     # examples fence-line banner typo (owner: examples repo)

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
if is_pdf_build:
    extensions.append('latex_writer')
else:
    # Render ```mermaid fences as diagrams (sphinx-mermaid from
    # requirements.txt). HTML-only: sphinxmermaid registers no LaTeX visitor,
    # so enabling it in PDF builds would fail on MermaidNode. In PDF builds
    # the fences fall back to plain text via the 'mermaid' lexer alias in
    # setup().
    extensions.append('sphinxmermaid')
    myst_fence_as_directive = ["mermaid"]
source_suffix = mcux_config.get_source_suffix()

# -- Options for rsvg-convert (SVG to PDF conversion) ---------------------
# The --unlimited flag lifts the default SVG size limit in rsvg-convert,
# preventing build failures on large SVG files from external repos.
rsvg_converter_args = ['--unlimited']

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
exclude_patterns = [
    # FreeMaster sub-files are {include}-only; only user_guide.md is a toctree source.
    # Processing them standalone causes xref failures for labels defined across files.
    'middleware/freemaster/doc/user_guide/[0-9]*.md',
    'middleware/freemaster/doc/user_guide/api/**',
    'middleware/freemaster/doc/user_guide/cfg/**',
    'middleware/freemaster/doc/user_guide/tsa/**',
    # erpc README uses GitHub root-relative paths (e.g. /erpc_c/transports) that
    # Sphinx misinterprets as cross-references and cannot resolve.
    'middleware/multicore/erpc/README.md',
]

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
    version_list = [(version, f"/mcuxsdk-internal/{('release-' + version.removesuffix('-lts')) if version != 'latest' else version}/html/") for version in versions_data]
else:
    version_list = [(version, f"/mcuxsdk/{version.removesuffix('-lts')}/html/") for version in versions_data]

html_context["versions"] = tuple(version_list)


# -- Options for notfound.extension ---------------------------------------
if is_internal_doc:
    notfound_urls_prefix = f"/mcuxsdk-internal/release-{version.removesuffix('-lts')}/html/" if is_release else "/mcuxsdk-internal/main/html/"
else:
    notfound_urls_prefix =  f"/mcuxsdk/{version.removesuffix('-lts')}/html/" if is_release else "/mcuxsdk/latest/html/"

# -- Options for vcs_link ------------------------------------------
if 'vcs_link' in extensions:
    vcs_link_prefixes = mcux_config.get_vcs_links()
    vcs_link_version = f"release/{version.removesuffix('-lts')}" if is_release else "main"

# -- Options for external_content ----------------------------------
if 'external_content' in extensions:
    external_content_contents = mcux_config.get_external_contents()
    external_content_keep = [
        # Images added to docs repo as ad-hoc fixes for external repo issues.
        # These must be kept so external_content doesn't delete them.
        'middleware/wireless/bluetooth/doc/Bluetooth Low Energy CCC Digital Key with Channel Sounding Application Note/images/serial_conn_2.jpg',
    ]

suppress_warnings = [
    "myst.header",              # Non-consecutive header level increase; H4 to H7
    'image.fetch',
    'duplicate_declaration.c',  # Duplicate C declarations from BLE API Reference doxygenfile directives
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

# -- Linkcheck configuration --------------------------------------------------

# nxp.com CDN returns HTTP 404 for browser-style User-Agents (any Mozilla/Chrome
# UA) but 200 for non-browser UAs.  Override only for nxp.com subdomains so
# real 404s on those hosts still surface.
linkcheck_request_headers = {
    "https://www.nxp.com/": {
        "User-Agent": "Python-urllib/3.11",
    },
    "https://www.nxp.com.cn/": {
        "User-Agent": "Python-urllib/3.11",
    },
    "https://mcuxpresso.nxp.com/": {
        "User-Agent": "Python-urllib/3.11",
    },
    "https://docs.mcuxpresso.nxp.com/": {
        "User-Agent": "Python-urllib/3.11",
    },
}

# GitHub renders anchors via JavaScript; the static HTML returned to linkcheck
# does not contain them.  Still check that the page itself exists (200).
linkcheck_anchors_ignore_for_url = [
    r"https://github\.com/.*",
    r"https://gitlab\.com/.*",
]

# Login-gated links that always redirect to a sign-in page: confirmed valid,
# but linkcheck cannot verify them without credentials.
linkcheck_ignore = [
    r"https://github\.com/.*/issues/new(/choose)?$",
]
