# Sample Project

This sample project is based on the one provided by the [Python Packaging User
Guide][packaging guide]'s [Tutorial on Packaging and Distributing
Projects][dist tutorial].  The source of the original sample project is
available [here][src].

[packaging guide]: https://packaging.python.org
[dist tutorial]: https://packaging.python.org/tutorials/packaging-projects/
[src]: https://github.com/pypa/sampleproject

This project is configured to what I personally like to use, namely:

* git
* GitHub
* namespace packaging
* pyproject.toml / setup.cfg / setup.py
* tox

[Note: The first part of this document is mainly template text. But the Chapter
"About ppf.sample" is actual explanation of why ppf.sample is how it is.]


# Installation

ppf.sample is available via [pypi](https://pypi.org):

```
pip install ppf.sample
```


# Still reading?

If you read this far, you're probably not here for the first time. If you use
and like this project, would you consider giving it a Github Star? (The button
is at the top of this website.) If not, maybe you're interested in one of
[my other projects](https://github.com/adrianschlatter/ppf.sample/blob/develop/docs/list_of_projects.md)?


# Contributing

Did you find a bug and would like to report it? Or maybe you've fixed it
already or want to help fixing it? That's great! Please read
[CONTRIBUTING](./CONTRIBUTING.md) to learn how to proceed.

To help ascertain that contributing to this project is a pleasant experience,
we have established a [code of conduct](./CODE_OF_CONDUCT.md). You can expect
everyone to adhere to it, just make sure you do as well.


# Change Log

* 0.1:	Initial demo.


# About ppf.sample

The name of this sample package is `sample` and it is configured to live
inside a _namespace_ named `ppf`. `ppf.sample` is a so-called _namespace_
_package_. Namespaces were invented to alleviate the package-name shortage
on pypi.org. I have claimed the `ppf`-namespace and I can publish packages
to it.

To install namespace packages, use:

```
pip install ppf.sample
pip install ppf.datamatrix
```

Import them in your code like this:

```
import ppf.sample
import ppf.datamatrix as dm
```

Note: `import ppf` does not do anything meaningful. In particular,
`ppf` is *not* a parent package having sub-packages.


## Package Structure

To create the namespace package `ppf.sample`, we use the following project
structure:

```
/
├── .github
│   └── workflows                   GitHub workflows
│       └── tox.yml                 Instruct GitHub to run tox
├── .gitignore                      Files git should ignore
├── LICENSE                         License of this package
├── MANIFEST.in                     What to include in the distribution
├── data                            Data
│   └── data_file
├── docs                            Documentation
│   ├── DEV_NOTES.md
│   ├── README.md                   README to show on GitHub
│   └── README_pypi.md              README to show on pypi.org
├── pyproject.toml                  Build tool configuration
├── setup.cfg                       Package configuration and tool options
├── setup.py                        Dummy script for backwards compatibility
├── src                             The sources
│   └── ppf                         Name of namespace
│       └── sample                  Name of package inside namespace
│           └── __init__.py
│           └── cli.py              A cmd-line utility
│           └── module.py
│           └── package_data.dat
│           └── utils.py            Helper functions for packaging
├── tests                           Unit tests package
│   ├── __init__.py
│   ├── test_cli.py                 Unit tests
│   └── test_myFunction.py          More unit tests
└── tox.ini                         tox configuration
```

## Build System

To avoid unnecessary incompatibilities, this project uses `pyproject.toml`,
`setup.cfg`, and `setup.py`.

On newer python version (>=3.7 in my experience), we could merge
`pyproject.toml`, `setup.cfg`, and `setup.py` into a single `pyproject.toml`.
However, on older versions (<=3.6) `setup.cfg` is necessary, and even
older python versions (<=3.5) need a (dummy) `setup.py`. 

### pyproject.toml

In this project, `pyproject.toml` declares the tools we want to use to
build the package and nothing more.

### setup.cfg

`setup.cfg` describes the package's [metadata] such as its name, version,
author, etc.

The [options] and [options.packages.find] sections
specify that this is a namespace package and where the build system should
look for the code. The [options] section also declares dependencies such
as minimum python version this package needs and which other packages `pip`
must install so that `ppf.sample` works.

[options.extras_require] lists additional groups of dependencies, such as
packages useful for development. I use the the test dependency group to
specify packages needed for testing. tox uses it to prepare the test envs:
Make sure it is correct.

Use [options.package_data] if your package provides data files.

If the package provides command-line utilities, you need 
[options.entry_points]. For every cmd-line tool you specify the name it
should have and the function to execute when the tool is called. The python
distribution tools will translate this to an executable suitable for the
operating system the package gets installed on.

#### Config Sections for Tools

We use `setup.cfg` to store the configuration of tools like `pytest`
(unittest runner), `flake8` (style-guide enforcement), and `check-manifest`
(manifest checking).

### setup.py

This is a dummy file that only imports the setup()-function and calls it.
Nothing to configure here. 


## Testing

Unit test are stored in tests/ and are run with `pytest`. The project is
configured to use `flake8` for code style verification and
`check-manifest` to verify that the files in the final package match those
in the repository.

`tox` is configured to build the package, install it in a fresh python
environment, and run the tests (`flake8`, `python setup.py check`,
`check-manifest`, and `pytest`). This is repeated for multiple python
versions (configurable in `tox.ini`). By default, tox also builds a source
distribution in every environment. If your package will be distributed as a
universal wheel, there is a quicker way: Build the wheel first, then tell tox
to always install this wheel into each python environment:

```shell
cd <root of repo>
python -m build --wheel
tox --parallel --installpkg dist/<the_wheel>
```

A test (on a slow computer) resulted in (11 + 283) seconds for build
+ ```tox --parallel --installpkg```, and 353 seconds for ```tox --parallel```.
Also, you usually want to test whether users will be able to install and run
your package, not whether they are able to build it.

A word of caution on ```tox --parallel```: It is ofter much quicker than not
using ```--parallel``` but sometimes it fails (in some environments) although
```tox``` without ```--parallel``` does not.

[GitHub workflows][workflows] live inside `.github/workflows/`. This
project pre-defines a workflow in `tox.yml` that instructs GitHub to run
`tox` on every pull request. Additionally, I usually require pull requests
for external developers to contribute into the develop branch and for
everyone pushing to master (i.e., when creating a release). This needs to
be configured on GitHub's web interface.

[workflows]: https://docs.github.com/en/actions/using-workflows/about-workflows


## Privacy vs contactability

Your personal email address is prone to land in the dirty hands of spammers.
Therefore, you want to publish it only when necessary. However, you need to
be contactable somehow, if only:

* for questions on your project, particularly licensing questions
* to enable anyone to applaud your work :-)

Therefore, I consider good practice to publish an email address in exactly
one, central place. That central place is your GitHub profile: If you need
to change the email address (e.g., because of too much spam), this is easy to
do. This also means that you do *not* publish your email address:

* in your commit messages
* in setup.py, setup.cfg, or similar
* on pypi

Instead, just provide a link to your (GitHub-) project. GitHub can also
help you with keeping your (private) email addresses private: Check your
settings to:

* tell GitHub to *not* show your email in web-based commits
* configure your git client to use your noreply GitHub address in commit
  messages
* inform GitHub (but no one else) what your private email addresses are
* tell GitHub to reject command-line commits that would reveal (one of) these
  private emails addresses


## Documentation

Write `docs/README.md` to show on GitHub. Write a separate (and simplified)
`docs/README_pypi.md` to show on [pypi.org][pypi]. Why not use the same?
Because you will run into problems with images: [pypi.org][pypi] cannot
access the images stored inside the package.

[pypi]: https://www.pypi.org
