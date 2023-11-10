# -*- coding: utf-8 -*-

"""
:author: Adrian Schlatter
"""

import sys


def export(obj):
    """
    Decorator that adds obj to __all__
    """

    mod = sys.modules[obj.__module__]
    mod.__all__ = getattr(mod, '__all__', []) + [obj.__name__]

    return obj


class ModuleName():
    """
    Helper class to work with namespace/package/module names.
    """

    def __init__(self, name):
        self.path = name.split('.')

    def __getitem__(self, slice):
        """Slice ModuleName by dots."""
        return ModuleName('.'.join(self.path[slice]))

    def __str__(self):
        """Convert to string."""
        return '.'.join(self.path)

    @property
    def normalized(self):
        """
        Normalize dots to underscores. Useful because python apparently does
        this with the names of namespace packages.
        """
        return '-'.join(self.path)
