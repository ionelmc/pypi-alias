#!/usr/bin/python
from __future__ import print_function

import os
import shutil
import subprocess
import sys
import tempfile


def main():
    name = subprocess.check_output(['python', 'setup.py', '--name']).strip()
    url = "https://pypi.python.org/pypi/%s/" % name
    description = subprocess.check_output(['python', 'setup.py', '--description']).strip()
    assert 'python' not in name
    if len(sys.argv) == 1:
        print("Usage: %s alias [setup.py arguments]" % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    alias = sys.argv[1]
    author = subprocess.check_output(['python', 'setup.py', '--author']).strip()
    author_email = subprocess.check_output(['python', 'setup.py', '--author-email']).strip()
    maintainer = subprocess.check_output(['python', 'setup.py', '--maintainer']).strip()
    maintainer_email = subprocess.check_output(['python', 'setup.py', '--maintainer-email']).strip()

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
