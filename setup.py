#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 26.03.2018 19:18
:Licence GNUv3
Part of regexp-inverse

"""

from setuptools import setup

setup(
    name='regexp_inverse',
    version='0.0.1',
    packages=['regexp_inverse'],
    # url='https://github.com/PatrikValkovic/grammpy',
    license='GNU General Public License v3.0',
    author='Patrik Valkovic',
    # download_url='https://github.com/PatrikValkovic/grammpy/archive/v1.0.1.tar.gz',
    author_email='patrik.valkovic@hotmail.cz',
    description='package that generates string based on the regular expression.',
    install_requires=['grammpy', 'grammpy-transforms', 'pyparsers'],
)
