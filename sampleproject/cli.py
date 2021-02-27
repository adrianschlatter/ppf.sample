# -*- coding: utf-8 -*-

"""
This module shows how to program a command-line tool using plumbum.

It consists of a tool named 'clt' (implemented in the class CommandLineTool)
that has a single sub-command 'say'.

>>> clt say --hello user
hello user

.. author: Adrian Schlatter
"""

from plumbum import cli
import pkg_resources  # part of setuptools


class CommandLineTool(cli.Application):
    """
    An example for a command line tool.

    Its name is 'clt' and it provides a single sub-command named 'say'.
    """

    PROGNAME = 'clt'
    VERSION = pkg_resources.require('sampleproject')[0].version

    def main(self, *args):
        pass


@CommandLineTool.subcommand('say')
class CLTSay(cli.Application):
    "Say something."

    something = ''

    @cli.switch('--hello')
    def hello(self):
        self.something = 'hello'

    @cli.switch('--bye')
    def bye(self):
        self.something = 'bye'

    def main(self, *args):
        print(self.something, *args)


def main():
    CommandLineTool.run()
