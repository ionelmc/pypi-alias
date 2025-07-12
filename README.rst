========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      -
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|

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

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/pypi-alias/v1.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/pypi-alias/compare/v1.0.0...main



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

Make sure you run ``pypi-alias`` in a directory that has a ``setup.py`` file.

Example::

    pypi-alias foobar sdist bdist_wheel
    twine upload dist\foobar*



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
