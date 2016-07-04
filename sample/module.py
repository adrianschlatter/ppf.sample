# -*- coding: utf-8 -*-
"""
A module providing functions, classes to be included in the package
"""


import numpy as np  # <= will *not* show up in package due to __init__.py


def myFunction(x):
    """Returns root of x."""
    
    return(np.sqrt(x))
