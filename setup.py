#!/usr/bin/env python
from functools import partial
import os
import sys

from os import path

from setuptools import setup, find_packages


name = 'tinbox-client'  # PyPI name
package_name = name.replace('-', '_')  # Python module name
package_path = 'src'  # Where does the package live?

here = path.dirname(path.abspath(__file__))

# Add src dir to path
sys.path.append(package_path)


# Get the long description from the relevant file
long_description = None

try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    pass


def get_version():
    """
    Get the version from a version module inside our package. This is
    necessary since we import our main modules in package/__init__.py,
    which will cause ImportErrors if we try to import package/version.py
    using the regular import mechanism.

    :return: Formatted version string
    """
    version = {}

    version_file = path.join(package_path, package_name, 'version.py')

    # exec the version module
    with open(version_file) as fp:
        exec(fp.read(), version)

    # Call the module function 'get_version'
    return version['get_version']()


setup(
    name=name,
    version=get_version(),
    author='Joar Wandborg',
    author_email='joar@5monkeys.se',
    url='https://github.com/5monkeys/tinbox-client',
    license='MIT',
    description='Tinbox client library',
    long_description=long_description,
    package_dir={'': package_path},  # Package lives in ./src
    packages=find_packages(package_path),
    install_requires=[
        'requests-oauthlib==0.4.2'
    ]
)