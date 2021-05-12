# A sample Python project

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

A sample project that exists as an aid to the [Python Packaging User
Guide][packaging guide]'s [Tutorial on Packaging and Distributing
Projects][distribution tutorial].

This project does not aim to cover best practices for Python project
development as a whole. For example, it does not provide guidance or tool
recommendations for version control, documentation, or testing.

[The source for this project is available here][src].

Most of the configuration for a Python project is done in the `setup.cfg` file,
an example of which is included in this project. You should edit this file
accordingly to adapt this sample project to your needs.

----

This is the README file for the project.

The file should use UTF-8 encoding and can be written using
[reStructuredText][rst] or [markdown][md use] with the appropriate [key set][md
use]. It will be used to generate the project webpage on PyPI and will be
displayed as the project homepage on common code-hosting services, and should be
written for that purpose.

Typical contents for this file would include an overview of the project, basic
usage examples, etc. Generally, including the project changelog in here is not a
good idea, although a simple “What's New” section for the most recent version
may be appropriate.

[packaging guide]: https://packaging.python.org
[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/
[src]: https://github.com/pypa/sampleproject
[rst]: http://docutils.sourceforge.net/rst.html
[md]: https://tools.ietf.org/html/rfc7764#section-3.5 "CommonMark variant"
[md use]: https://packaging.python.org/specifications/core-metadata/#description-content-type-optional

----

# Personal best practices

## Testing

Write unittests. Use tox.

## Privacy vs contactability

Your personal email address is prone to land in the dirty hands of spammers.
Therefore, you want to publish it only when necessary. However, you need to
be contactable somehow, if only:

* for questions on your project, particularly licensing questions
* to enable anyone to applaud your work ;)

Therefore, I consider good practice to publish an email address in exactly
one, central place. That central place is your GitHub profile: If you need
to change the email address (e.g., because of too much spam), this is easy to
do. This also means that you do *not* publish your email address:

* in your commit messages
* in setup.py, setup.cfg, or similar
* on pypi

Instead, just provide a link to your (GitHub-) project. GitHub can also help you
with keeping your (private) email addresses private: Check the email settings
to:

* tell GitHub to *not* show your email in web-based commits
* configure your git client to use your noreply GitHub address in commit
  messages
* inform GitHub (but no one else) what your private email addresses are
* tell GitHub to reject command-line commits that would reveal (one of) your
  private emails addresses

## Distribution

Write README.md so that it works simultaneously on GitHub and pypi.org.
