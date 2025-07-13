========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |github-actions|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|

.. |github-actions| image:: https://github.com/ionelmc/pypi-alias/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/ionelmc/pypi-alias/actions

.. |version| image:: https://img.shields.io/pypi/v/pypi-alias.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pypi-alias

.. |wheel| image:: https://img.shields.io/pypi/wheel/pypi-alias.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pypi-alias

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pypi-alias.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pypi-alias

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pypi-alias.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pypi-alias

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/pypi-alias/v2.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/pypi-alias/compare/v2.0.0...main



.. end-badges

A small utility to make alias distributions on PyPI.

It will create an "empty" package with a different name (the "alias") that depends on the package in your current working directory.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install pypi-alias

You can also install the in-development version with::

    pip install https://github.com/ionelmc/pypi-alias/archive/master.zip

Usage
=====

You can use ``pypi-alias`` with a distribution file (a ``.whl`` file or a sdist) or with a path, as long as it has a ``pyproject.toml``
with build configuration in it.

Example, if say, you have a ``foobar`` package, and you want to make an alias with name ``python-foobar``, assuming your in the checkout
path::

    pypi-alias python-foobar

You can specify a version::

    pypi-alias python-foobar --alias-version=1.0

You can use a dist file::

    pypi-alias python-foobar --alias-version=1.0 dist/foobar-1.2.3.tar.gz

And you can also add some build options for the resulting alias package (example: only build sdist in a different path)::

    pypi-alias python-foobar --alias-version=1.0 dist/foobar-1.2.3.tar.gz -- --dist --outdir=aliased-dist

The resulting files are in ``dist\``, assuming you haven't used ``--outdir``, you can upload them with twine::

    twine upload dist\python-foobar*

Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
