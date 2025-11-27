'''MCUXpresso Document Extension
   Copyright 2024 NXP
   All rights reserved.

   SPDX-License-Identifier: BSD-3-Clause
'''
#!/usr/bin/python3
import os,sys
import shutil
import shlex
import argparse
import subprocess
from pathlib import Path
from textwrap import dedent
import json
import yaml
import time
from west.commands import WestCommand

DOC_PATH = Path(__file__).absolute().parents[2]
script_dir = DOC_PATH / 'scripts'

with open(DOC_PATH / '_cfg' / 'user_config.yml', 'r', encoding='utf-8') as f:
    MODULE_NAMES = yaml.safe_load(f)['modules'].keys()

LF_STRING = "\n"
DOC_USAGE = f'''
Tags:
    Modules: {LF_STRING.join(MODULE_NAMES)}
    
Build Modes (affects driver doxygen projects only):
    original: Use breathe to integrate Doxygen XML (default)
    html: Generate Doxygen HTML directly for drivers (low memory)
    sphinx: Create separate Sphinx projects for drivers (distributed memory)
    
Note: 
    - Non-driver projects follow their 'mode' setting in user_config.yml
    - PDF/LaTeX builds always use breathe mode for all projects
    - Multiple doxygen modes can coexist in the same build
'''

def add_new_arguments(parser):

    parser.add_argument(
        '-t', '--tags', action='store', type=str, default='development',
        help='Tags for the document creation. Tags are joined by "," and regex format. '
            'For example, -t mid_.*,gsd will pick the modules starting with mid_ and gsd module.'
    )
    parser.add_argument(
        '-b', '--build_dir', action='store', type=str, default='_build',
        help='Build directory for the document creation'
    )
    parser.add_argument(
        '--sphinx_opts', action='store', type=str, default='-j auto --keep-going -T',
        help='Additional options for sphinx-build'
    )
    parser.add_argument(
        '--sphinx_extra_opts', action='store', type=str, default='',
        help='Additional options for sphinx-build'
    )
    parser.add_argument(
        '--latexmkopts', action='store', type=str, default=' -halt-on-error -no-shell-escape',
        help='Additional options for latexmk'
    )
    parser.add_argument(
        '--branch', action='store', type=str, default='main',
        help='Branch for the document creation'
    )
    parser.add_argument(
        '--revision', action='store', type=str, default='851c5ddabe8',
        help='Revision for the document creation'
    )
    parser.add_argument(
        '-d', '--defines', action='store', type=str, default='',
        help='Additional defines for the document creation, e.g -d a=b,c=d'
    )
    parser.add_argument(
        '--internal', action='store_true', default=False,
        help='Internal document creation'
    )
    parser.add_argument(
        '--example_scope', action='store', type=str, default='',
        help='Examples for document creation, like examples/demo_apps'
    )
    parser.add_argument(
        '--doxygen', action='store_true', default=False,
        help='enable doxygen run'
    )

    # Add board parameter to the doc command
    parser.add_argument(
        "--board", action='store', type=str, default='',
        help="Board target for building board-specific documentation")
    
    # Add build mode parameter
    parser.add_argument(
        '--build_mode', action='store', type=str, 
        choices=['original', 'html', 'sphinx'], default='sphinx',
        help='Documentation build mode for driver projects: original (breathe), html (direct doxygen), sphinx (separate projects)'
    )
    
    # Add memory optimization options
    parser.add_argument(
        '--low_memory', action='store_true', default=False,
        help='Enable low memory mode (automatically selects html mode for drivers)'
    )
    
    return parser


def args_to_cmdline(args, exclude_keys=[]):

    exclude_keys.extend(['target', 'command'])
    cmdline = []
    for key, value in vars(args).items():
        if value in [None, False, 0] or key in exclude_keys:
            continue  # Skip None values
        cmdline.append(f"--{key}")
        if isinstance(value, bool):
            if not value:
                cmdline.pop()  # Remove flag if False
        else:
            cmdline.append(str(value))
    return cmdline


def format_time(seconds):
    """Simple time formatter"""
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes}m {secs}s"


class MCUXDoc(WestCommand):
    '''MCUXpresso Document Extension'''
    def __init__(self):
        super().__init__(
            name='doc',
            help='Generate MCUXpresso SDK Document',
            description=dedent('''
            Use this command to generate SDK documentation.'''))

    def do_add_parser(self, parser_adder):
        # This is a bit of boilerplate, which allows you full control over the
        # type of argparse handling you want. The "parser_adder" argument is
        # the return value of an argparse.ArgumentParser.add_subparsers() call.

        parser = parser_adder.add_parser(
            self.name,
            help=self.help,
            description=self.description,
            usage=DOC_USAGE,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

        parser.add_argument(
            'target', action='store', type=str,
            choices=['clean', 'html', 'latex', 'doxygen', 'pdf', 'config', 'view', 'validate', 'all'],
            help='Target for the document creation'
        )
        
        return add_new_arguments(parser)

    def _validate_user_config(self):
        from jsonschema import validate, ValidationError

        with open(DOC_PATH / '_cfg' / 'mcux_doc_config_schema.json', 'r', encoding='utf-8') as f:
            schema = json.load(f)
        
        with open(DOC_PATH / '_cfg' / 'user_config.yml', 'r', encoding='utf-8') as f:
            user_config = yaml.safe_load(f)
        
        try:
            validate(user_config, schema)
        except ValidationError as e:
            self.err(f"User config validation failed: {e.path}, {e.message}")
            return None
        
        return user_config

    def do_run(self, args, unknown):
        # Start overall timing
        overall_start = time.time()

        self.banner("MCUX Document Creation")
        self.inf(f'  Target: {args.target}')
        self.inf(f'  Tags: {args.tags}')
        self.inf(f'  Driver Build Mode: {args.build_mode}')
        if args.low_memory:
            self.inf(f'  Low Memory Mode: Enabled')
        self.inf(f'  Note: Non-driver projects use their configured mode from user_config.yml')
        self.inf(f'  Note: PDF/LaTeX builds will use breathe mode for all projects')

        # Auto-select html mode for low memory
        if args.low_memory and args.build_mode == 'original':
            args.build_mode = 'html'
            self.inf(f'  Auto-selected html mode for drivers due to low memory')

        targets = []
        if args.target == 'clean':
            targets = ['clean']
        elif args.target == 'view':
            targets = ['view']
        elif args.target == 'config':
            targets = ['config']
        elif args.target != 'all':
            targets = ['clean', 'config', args.target]
        else:
            targets = ['all']

        for target in targets:
            self.banner(f'Target Execution - {target}')
            target_start = time.time()
            
            if target == 'clean':
                self.inf("Cleaning document directory")
                build_dir = DOC_PATH / args.build_dir
                if build_dir.exists():
                    shutil.rmtree(build_dir)
                    
            elif target == 'view':
                html_path = Path(args.build_dir) / 'html' / 'index.html'
                if html_path.exists():
                    replace_entry = str(Path(args.build_dir) / "html").replace("\\", "/")
                    cmd = f'python -m http.server -d {replace_entry} --bind 127.0.0.1'
                    self.inf('Hosting HTML: ' + cmd)
                    subprocess.check_call(shlex.split(cmd))
                else:
                    self.err('HTML folder does not exist')
                    
            elif target == 'config':
                defines = args.defines
                tags = 'internal_doc' if args.internal else 'external_doc'
                if args.doxygen:
                    tags += ',' + 'doxygen'
                if args.tags:
                    tags += ',' + args.tags

                # Add build mode to defines
                build_mode_defines = f'BUILD_MODE={args.build_mode}'
                if args.low_memory:
                    build_mode_defines += ',LOW_MEMORY=1'
                if defines:
                    defines += ',' + build_mode_defines
                else:
                    defines = build_mode_defines

                sphinx_opts = args.sphinx_opts

                cmd = shlex.split(
                    f'cmake -GNinja -B{args.build_dir} -S . '
                    f'-DDOC_TAG={tags} -DDOC_DEFINE={defines} '
                    f'-DSPHINXOPTS="{sphinx_opts}" '
                    f'-DSPHINXOPTS_EXTRA="{args.sphinx_extra_opts}" '
                    f'-DLATEXMKOPTS="{args.latexmkopts}" '
                    f'-DEXAMPLE_SCOPE="{args.example_scope}" '
                    f'-DBOARD_TARGET="{args.board}" '
                    f'-DBUILD_MODE="{args.build_mode}" '
                    f'-DDOCGEN_BRANCH={args.branch} '
                    f'-DDOCGEN_REV={args.revision} '
                    f'-DSPHINX_CONF_DIR=.'
                )
                
                if subprocess.check_call(cmd, cwd=DOC_PATH):
                    self.err("Failed to configure document")
                    
            elif target == 'validate':
                if not self._validate_user_config():
                    self.err("Failed to validate user_config.yml")
                    
            elif target == 'all':
                # Call build_all_docs.py script
                build_dir = DOC_PATH / args.build_dir
                if build_dir.exists():
                    shutil.rmtree(build_dir)
                
                if args.board:
                    build_all_cmd = [
                        sys.executable, 
                        str(script_dir / "build_all_docs.py")
                    ] + args_to_cmdline(args)
                else:
                    build_all_cmd = [
                        sys.executable, 
                        str(script_dir / "build_all_docs.py")
                    ] + args_to_cmdline(args, ['board'])
                
                try:
                    result = subprocess.run(build_all_cmd, check=True)
                    if result.returncode != 0:
                        self.err(f"build_all_docs.py failed with exit code: {result.returncode}")
                        return 1
                except subprocess.CalledProcessError as e:
                    self.err(f"Error running build_all_docs.py: {e}")
                    self.err(f"Exit code: {e.returncode}")
                    return 1
                
                return 0
            else:
                cmd = shlex.split(f'cmake --build {args.build_dir} --target {target}')
                if subprocess.check_call(cmd, cwd=DOC_PATH):
                    self.err("Failed to build document")
            
            # Print timing for this target
            target_time = time.time() - target_start
            self.inf(f"⏱️  {target} completed in {format_time(target_time)}")
        
        # Print overall timing
        overall_time = time.time() - overall_start
        self.banner("Build Complete")
        self.inf(f"⏱️  Total time: {format_time(overall_time)}")
        
        return 0
