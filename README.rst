===============================
pypi-alias
===============================

.. list-table::
    :stub-columns: 1

    * - package
      - |version| |downloads|

..
    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | |coveralls| |codecov| |landscape| |scrutinizer|
    |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/pypi-alias/badge/?style=flat
    :target: https://readthedocs.org/projects/pypi-alias
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/ionelmc/pypi-alias/master.svg?style=flat&label=Travis
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/pypi-alias

.. |appveyor| image:: https://img.shields.io/appveyor/ci/ionelmc/pypi-alias/master.svg?style=flat&label=AppVeyor
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/pypi-alias

.. |coveralls| image:: http://img.shields.io/coveralls/ionelmc/pypi-alias/master.svg?style=flat&label=Coveralls
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/pypi-alias

.. |codecov| image:: http://img.shields.io/codecov/c/github/ionelmc/pypi-alias/master.svg?style=flat&label=Codecov
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/pypi-alias

.. |landscape| image:: https://landscape.io/github/ionelmc/pypi-alias/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/pypi-alias/master
    :alt: Code Quality Status

.. |version| image:: http://img.shields.io/pypi/v/pypi-alias.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pypi-alias

.. |downloads| image:: http://img.shields.io/pypi/dm/pypi-alias.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/pypi-alias

.. |wheel| image:: https://pypip.in/wheel/pypi-alias/badge.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pypi-alias

.. |supported-versions| image:: https://pypip.in/py_versions/pypi-alias/badge.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pypi-alias

.. |supported-implementations| image:: https://pypip.in/implementation/pypi-alias/badge.svg?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/pypi-alias

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/pypi-alias/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/pypi-alias/

A small utility to make alias distributions on PyPI.

It will create an "empty" package with a different name (the "alias") that depends on the package in your current working directory.

* Free software: BSD license

Installation
============

::

    pip install pypi-alias

Documentation
=============

Make sure you run ``pypi-alias`` in a directory that has a ``setup.py`` file.

Usage::

    pypi-alias alternate-name register sdist bdist_wheel upload
