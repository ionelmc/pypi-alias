#!/usr/bin/python
from __future__ import print_function

import os
import shutil
import subprocess
import sys
import tempfile


def run_command(params):
    output = subprocess.check_output(params, encoding="utf-8")
    return output.strip()


def main():
    name = run_command(['python', 'setup.py', '--name'])
    url = "https://pypi.python.org/pypi/%s/" % name
    description = run_command(['python', 'setup.py', '--description'])
    assert 'python' not in name
    if len(sys.argv) == 1:
        print("Usage: %s alias [setup.py arguments]" % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    alias = sys.argv[1]
    author = run_command(['python', 'setup.py', '--author'])
    author_email = run_command(['python', 'setup.py', '--author-email'])
    maintainer = run_command(['python', 'setup.py', '--maintainer'])
    maintainer_email = run_command(['python', 'setup.py', '--maintainer-email'])

    try:
        path = tempfile.mkdtemp()
        os.chdir(path)
        with open(os.path.join(path, 'setup.cfg'), 'wb') as fh:
            fh.write(b"""[bdist_wheel]
universal = 1
""")
        with open(os.path.join(path, 'setup.py'), 'wb') as fh:
            fh.write(b"""# encoding: utf8

from setuptools import setup


setup(
    author=%(author)r,
    author_email=%(author_email)r,
    description=%(description)r,
    install_requires=[%(name)r],
    long_description='''Use `%(name)s <%(url)s>`_ instead.''',
    maintainer=%(author)r,
    maintainer_email=%(author_email)r,
    name=%(alias)r,
    platforms=['all'],
    py_modules=['wheel-platform-tag-is-broken-on-empty-wheels-see-issue-141'],
    url=%(url)r,
    version="0.0",
    zip_safe=False,
)
""" % locals())

        subprocess.call(['python', 'setup.py'] + sys.argv[2:])
    finally:
        shutil.rmtree(path)

if __name__ == '__main__':
    main()
