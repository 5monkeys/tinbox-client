#!/usr/bin/env python
import sys
from os import path
from setuptools import setup, find_packages

src = path.join(path.dirname(path.abspath(__file__)), 'src')
sys.path.append(src)

name = 'trak_client'
version = __import__(name).__version__

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
