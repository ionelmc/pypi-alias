import os

import pytest

from pypi_alias.cli import run


@pytest.mark.parametrize(
    "extras",
    [
        [],
        ["--dirty"],
    ],
)
def test_main(extras):
    run(["foobar", "--alias-version=1.2.3", *extras])
    files = os.listdir("dist")  # noqa
    assert "foobar-1.2.3-py3-none-any.whl" in files
    assert "foobar-1.2.3.tar.gz" in files
