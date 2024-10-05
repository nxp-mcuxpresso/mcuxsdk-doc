#!/usr/bin/python3
from pathlib import Path
import argparse
import shutil, shlex
import subprocess
from west.commands import WestCommand
from west.commands import CommandError
from west.manifest import Manifest
from west.util import west_topdir

import os,yaml,logging

from pathlib import *
from textwrap import dedent            # just for nicer code indentation
from west import log
import subprocess

DOC_PATH = Path(__file__).absolute().parents[2]

with open(DOC_PATH / '_cfg/user_config.yml', 'r', encoding='utf-8') as f:
    MODULE_NAMES = yaml.safe_load(f)['modules'].keys()

DOC_USAGE = f'''
Tags:
    Modules: {"\n".join(MODULE_NAMES)}
'''

class MCUXDoc(WestCommand):
    def __init__(self):
        super().__init__(
            name='doc',
            help='Install conditional personal git configuration to global git configuration, which translates the Github URL to Bitbucket URL',
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

        parser.add_argument('target', action='store', type=str, choices=['clean', 'html', 'latex', 'doxygen', 'pdf', 'config'], help='Target for the document creation')
        parser.add_argument('-t', '--tags',  action='store', type=str, default='development', help='Tags for the document creation. Tags are joined by "," and regex format. For example, -t mid_.*,gsd will pick the modules starting with mid_ and gsd module.')
        parser.add_argument('-b', '--build_dir',action='store', type=str, default='_build', help='Build directory for the document creation')
        parser.add_argument('--sphinx_opts', action='store', type=str, default='-j auto --keep-going -T', help='Additional options for sphinx-build')
        parser.add_argument('--sphinx_extra_opts', action='store', type=str, default='', help='Additional options for sphinx-build')
        parser.add_argument('--latexmkopts', action='store', type=str, default=' -halt-on-error -no-shell-escape', help='Additional options for latexmk')
        parser.add_argument('--branch', action='store', type=str, default='main', help='Branch for the document creation')
        parser.add_argument('--revision', action='store', type=str, default='851c5ddabe8', help='Revision for the document creation')

        return parser           # gets stored as self.parser

    def do_run(self, args, unknown_args):

        self.banner("MCUX Document Creation")
        self.inf(f'  Target: {args.target}')
        self.inf(f'  Tags: {args.tags} Find detailed tags in docs/_cfg/user_config.yml')

        targets = []
        if args.target == 'clean':
            targets = ['clean']
        elif args.target == 'config':
            targets = ['config']
        else:
            targets = ['config', args.target]

        for target in targets:
            self.banner(f'Target Execution - {args.target}')
            if target == 'clean':
                self.inf("Clean the document directory")
                build_dir = DOC_PATH / args.build_dir
                if build_dir.exists():
                    shutil.rmtree(build_dir)
            elif target == 'config':
                cmd = shlex.split(f'cmake -GNinja -B{args.build_dir} -S . -DDOC_TAG={args.tags} -DSPHINXOPTS="{args.sphinx_opts}" -DSPHINXOPTS_EXTRA="{args.sphinx_extra_opts}" -DLATEXMKOPTS="{args.latexmkopts}" -DDOCGEN_BRANCH={args.branch} -DDOCGEN_REV={args.revision} -DSPHINX_CONF_DIR=.')
                if subprocess.check_call(cmd, cwd=DOC_PATH):
                    self.err("Failed to configure the document with \n" + cmd)
            else:
                cmd = shlex.split(f'cmake --build {args.build_dir} --target {args.target}')
                if subprocess.check_call(cmd, cwd=DOC_PATH):
                    self.err("Failed to build the document with \n" + cmd)

