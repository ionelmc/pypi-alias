import os

import pytest

from pypi_alias.cli import main


@pytest.mark.parametrize('extras', [
    [],
    ['--dirty'],
])
def test_main(extras):
    main(['foobar', 'bdist_wheel', 'sdist', '--version=1.2.3'] + extras)
    files = os.listdir('dist')
    assert 'foobar-1.2.3-py2.py3-none-any.whl' in files
    assert 'foobar-1.2.3.tar.gz' in files
