#!/usr/bin/env python
import os
import sys
import warnings

from setuptools import setup, find_packages

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
sys.path.append(src)

name = 'trak_client'

warnings.warn('Setting os.environ[\'TRAK_CLIENT_VERSION_ONLY\'] in '
              'order to import trak___version__. Will unset after import.')
os.environ.update({'TRAK_CLIENT_VERSION_ONLY': 'True'})
version = __import__(name).__version__
del os.environ['TRAK_CLIENT_VERSION_ONLY']

import os
os.chdir(src)

setup(
    name=name,
    version=version,
    author='Joar Wandborg',
    author_email='joar@5monkeys.se',
    packages=find_packages(exclude=['_*']),
    install_requires=[
        'requests-oauthlib==0.4.2'
    ]
)
