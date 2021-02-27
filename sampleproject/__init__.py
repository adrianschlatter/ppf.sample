"""
Sample
++++++

Sample is a package demonstrating how to package Python code
"""
# flake8: noqa

# import every function, class, etc. that should be visible in the package
from .module import *

del module      # module will not show up in package namespace
del utils
