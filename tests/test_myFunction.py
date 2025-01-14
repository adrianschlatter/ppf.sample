# -*- coding: utf-8 -*-
"""
A template script demonstrating how to do unit testing.

All files in this directory named "test_*.py" are automatically identified
as unittests by 'pytest'.
"""

import unittest
import ppf.sample as dut


class Test_myFunction(unittest.TestCase):
    """Test something. All methods in this class named 'test_XXX' are assumed
    to be tests."""

    def setUp(self):
        """Code that will be run before each test in this class"""
        pass

    def test_known_property(self):
        """Square of result of my_function(x) must be x."""

        self.assertAlmostEqual(dut.my_function(5.)**2, 5.)


if __name__ == '__main__':
    unittest.main()
