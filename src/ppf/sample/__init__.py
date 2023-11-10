# -*- coding: utf-8 -*-

"""
Sample
++++++

Sample is a package demonstrating how to package Python code
"""
try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version
from .utils import ModuleName


__version__ = version(str(ModuleName(__name__).normalized))

# import every function, class, etc. that should be visible in the package
from .module import *

del module
del utils
