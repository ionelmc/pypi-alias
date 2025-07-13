import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional

import pkginfo
from build import ProjectBuilder
from build.env import DefaultIsolatedEnv


def check_output(params):
    output = subprocess.check_output(params, encoding="utf-8")
    return output.strip()


parser = argparse.ArgumentParser(
    description="Generates a dist that copies some of the metadata, depends on the original package and has a given name (the alias)."
)
parser.add_argument("alias_name", help="Package name to use (the alias).")
parser.add_argument("source_path", nargs="?", default=Path(), type=Path, help="Path to source package directory or dist (wheel or sdist).")
parser.add_argument("--alias-version", "-a", default=None, help="The version of the aliased package. Defaults to source package's version.")
parser.add_argument("--dirty", action="store_true", help="Don't cleanup the tmpdir.")


def run(args=None):
    options, passthrough_args = parser.parse_known_args(args=args)
    version: Optional[str] = options.alias_version
    path: Path = options.source_path
    if path.is_file():
        Distribution = pkginfo.Wheel if path.suffix == ".whl" else pkginfo.SDist
        dist = Distribution(os.fspath(path))
    else:
        with DefaultIsolatedEnv() as env:
            builder = ProjectBuilder.from_isolated_env(env, path)
            env.install(builder.build_system_requires)
            env.install(builder.get_requires_for_build("sdist"))
            dist_path = builder.build("sdist", "dist")

        dist = pkginfo.SDist(dist_path)

    name = dist.name
    version = version or dist.version
    url = f"https://pypi.python.org/pypi/{name}/"
    description = dist.summary
    long_description = f"Use `{name} <{url}>`_ instead."
    pyproject_toml = f"""
[build-system]
requires = ["setuptools>=69"]
build-backend = "setuptools.build_meta"

[project]
name = {options.alias_name!r}
version = {version!r}
description = {description!r}
readme = {{ file = "README", content-type = "text/x-rst" }}
"""

    tmp_path = Path(tempfile.mkdtemp())
    project_path = Path.cwd().resolve()
    output_path = project_path / "dist"
    output_path.mkdir(exist_ok=True)

    try:
        tmp_path.joinpath("dist").symlink_to(output_path, target_is_directory=True)
        os.chdir(tmp_path)

        with Path(tmp_path, "README").open("w", encoding="utf-8") as fh:
            fh.write(long_description)

        with Path(tmp_path, "pyproject.toml").open("w", encoding="utf-8") as fh:
            fh.write(pyproject_toml)
            if dist.requires_python:
                fh.write(f"""
requires-python = {dist.requires_python!r}
""")
        print(f"-> Generated pyproject.toml code in {tmp_path}:")
        print(pyproject_toml)
        print(f"-> Running: build {' '.join(passthrough_args)}")
        subprocess.call([sys.executable, "-mbuild", *passthrough_args])
    finally:
        os.chdir(project_path)
        if not options.dirty:
            shutil.rmtree(tmp_path)
