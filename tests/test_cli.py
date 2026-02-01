# -*- coding: utf-8 -*-
"""
test command-line tool
"""

import unittest
from unittest.mock import patch
from ppf.sample import cli


class Test_CLI(unittest.TestCase):
    """Test CLI"""

    def setUp(self):
        """Code that will be run before each test in this class"""
        pass

    def test_system_exit(self):
        """Running `cli` will end in the tool exiting with SystemExit"""
        try:
            cli.main()
        except SystemExit:
            pass
        else:
            self.fail('Expected System Exit')

    def test_say(self):
        """Run say"""
        cli.CommandLineTool.run(['nameoftool', 'say', '--hello', 'world'],
                                exit=False)

    def test_say_bye(self):
        """Run say"""
        cli.CommandLineTool.run(
                ['nameoftool', 'say', '--bye', 'world'],
                exit=False)

    def test_say_colloquial(self):
        """Run say with colloquial config"""
        # patch cli.Config contex manager to return dict with colloquial True:
        with patch('ppf.sample.cli.cli.Config') as mock_config:
            mock_config.return_value.__enter__.return_value = {
                                                        'colloquial': 'True'}
            cli.CommandLineTool.run(['nameoftool', 'say', '--hello', 'world'],
                                    exit=False)


if __name__ == '__main__':
    unittest.main()
