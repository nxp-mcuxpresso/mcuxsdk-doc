'''MCUXpresso Document Extension
   Copyright 2024 NXP
   All rights reserved.

   SPDX-License-Identifier: BSD-3-Clause
'''
#!/usr/bin/python3
import os
import shutil
import shlex
import argparse
import subprocess
from pathlib import Path
from textwrap import dedent  # just for nicer code indentation

import yaml
from west.commands import WestCommand

DOC_PATH = Path(__file__).absolute().parents[2]

with open(DOC_PATH / '_cfg/user_config.yml', 'r', encoding='utf-8') as f:
    MODULE_NAMES = yaml.safe_load(f)['modules'].keys()

LF_STRING = "\n"
DOC_USAGE = f'''
Tags:
    Modules: {LF_STRING.join(MODULE_NAMES)}
'''

class MCUXDoc(WestCommand):
    '''MCUXpresso Document Externsion'''
    def __init__(self):
        super().__init__(
            name='doc',
            help='Generate MCUXpresso SDK Document',
            description=dedent('''
            Use this command to set up sdk development repos.'''))

    def do_add_parser(self, parser_adder):
        # This is a bit of boilerplate, which allows you full control over the
        # type of argparse handling you want. The "parser_adder" argument is
        # the return value of an argparse.ArgumentParser.add_subparsers() call.


        parser = parser_adder.add_parser(self.name,
                                 help=self.help,
                                 description=self.description,
                                 usage=DOC_USAGE,
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        parser.add_argument(
            'target', action='store', type=str,
            choices=['clean', 'html', 'latex', 'doxygen', 'pdf', 'config', 'view'],
            help='Target for the document creation'
        )
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

        return parser           # gets stored as self.parser

    def do_run(self, args, unknown):

        self.banner("MCUX Document Creation")
        self.inf(f'  Target: {args.target}')
        self.inf(f'  Tags: {args.tags} Find detailed tags in docs/_cfg/user_config.yml')

        targets = []
        if args.target == 'clean':
            targets = ['clean']
        elif args.target == 'view':
            targets = ['view']
        elif args.target == 'config':
            targets = ['config']
        else:
            targets = ['clean', 'config', args.target]

        for target in targets:
            self.banner(f'Target Execution - {target}')
            if target == 'clean':
                self.inf("Clean the document directory")
                build_dir = DOC_PATH / args.build_dir
                if build_dir.exists():
                    shutil.rmtree(build_dir)
            elif target == 'view':
                if os.path.exists(os.path.join(args.build_dir, 'html', 'index.html')):
                    replace_entry = os.path.join(args.build_dir, "html").replace("\\", "/")
                    cmd = f'python -m http.server -d {replace_entry} --bind 127.0.0.1'
                    self.inf('Host HTML: ' + cmd)
                    subprocess.check_call(shlex.split(cmd))
                else:
                    self.err('Html folder is not existed')
            elif target == 'config':
                defines = args.defines
                tags = 'internal_doc' if args.internal else 'external_doc'
                if args.tags:
                    tags += ',' + args.tags

                cmd = shlex.split(f'cmake -GNinja -B{args.build_dir} -S . '
                                  f'-DDOC_TAG={tags} -DDOC_DEFINE={defines} '
                                  f'-DSPHINXOPTS="{args.sphinx_opts}" -DSPHINXOPTS_EXTRA="{args.sphinx_extra_opts}" '
                                  f'-DLATEXMKOPTS="{args.latexmkopts}" '
                                  f'-DEXAMPLE_SCOPE="{args.example_scope}" '
                                  f'-DDOCGEN_BRANCH={args.branch} -DDOCGEN_REV={args.revision} -DSPHINX_CONF_DIR=.')
                if subprocess.check_call(cmd, cwd=DOC_PATH):
                    self.err("Failed to configure the document with \n" + cmd)
            else:
                cmd = shlex.split(f'cmake --build {args.build_dir} --target {args.target}')
                if subprocess.check_call(cmd, cwd=DOC_PATH):
                    self.err("Failed to build the document with \n" + cmd)
