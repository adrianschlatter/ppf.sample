# -*- coding: utf-8 -*-
"""
test command-line tool
"""

import unittest
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


if __name__ == '__main__':
    unittest.main()
