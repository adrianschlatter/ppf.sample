# Testing

needs setuptools>=40.5.0 because we run `python setup.py check -m` and
earlier version do not understand the [option.data_files] section in
our setup.cfg.
