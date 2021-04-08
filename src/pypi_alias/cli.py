import argparse
import os
import shutil
import subprocess
import tempfile


def check_output(params):
    output = subprocess.check_output(params, encoding="utf-8")
    return output.strip()


parser = argparse.ArgumentParser(description="Generate and run a setup.py that aliases to the current setup.py's package name.")
parser.add_argument('name', help='Package name to use (the alias).')
parser.add_argument('--version', '-v', default='0.0', help='Version to write in the generated setup.py')
parser.add_argument('--dirty', action='store_true', help="Don't cleanup the tmpdir.")


def main(args=None):
    options, passthrough_args = parser.parse_known_args(args=args)

    name = check_output(['python', 'setup.py', '--name'])
    url = "https://pypi.python.org/pypi/%s/" % name
    description = check_output(['python', 'setup.py', '--description'])
    author = check_output(['python', 'setup.py', '--author'])
    author_email = check_output(['python', 'setup.py', '--author-email'])
    maintainer = check_output(['python', 'setup.py', '--maintainer'])
    maintainer_email = check_output(['python', 'setup.py', '--maintainer-email'])

    long_description = f'Use `{name} <{url}>`_ instead.'
    setup_py = f"""# encoding: utf8

from setuptools import setup


setup(
    author={author!r},
    author_email={author_email!r},
    description={description!r},
    install_requires=[{name!r}],
    long_description={long_description!r},
    maintainer={maintainer!r},
    maintainer_email={maintainer_email!r},
    name={options.name!r},
    platforms=['all'],
    url={url!r},
    version={options.version!r},
    zip_safe=False,
)
"""

    tmp_path = tempfile.mkdtemp()
    project_path = os.path.abspath(os.getcwd())
    output_path = os.path.join(project_path, 'dist')
    os.makedirs(output_path, exist_ok=True)

    try:
        os.symlink(output_path, os.path.join(tmp_path, 'dist'), target_is_directory=True)
        os.chdir(tmp_path)
        with open(os.path.join(tmp_path, 'setup.cfg'), 'w', encoding="utf-8") as fh:
            fh.write("""[bdist_wheel]
universal = 1
""")
        with open(os.path.join(tmp_path, 'README'), 'w', encoding="utf-8") as fh:
            fh.write(long_description)

        with open(os.path.join(tmp_path, 'setup.py'), 'w', encoding="utf-8") as fh:
            fh.write(setup_py)

        print(f'-> Generated setup.py code in {tmp_path}:')
        print(setup_py)
        print(f'-> Running: python setup.py {" ".join(passthrough_args)}')
        subprocess.call(['python', 'setup.py'] + passthrough_args)
    finally:
        os.chdir(project_path)
        if not options.dirty:
            shutil.rmtree(tmp_path)
