#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup
from setuptools import find_packages

version = '0.1.0'

if os.path.isdir("panoramisk") and not os.path.exists("trio_panoramisk"):
    os.symlink("panoramisk","trio_panoramisk")

install_requires = ['trio']
test_requires = [
    'pytest-trio', 'coverage', 'coveralls'
]

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='trio_panoramisk',
    version=version,
    description="trio-based library to play with asterisk",
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications :: Telephony',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['trio', 'asterisk', 'voip'],
    author='Matthias Urlichs',
    author_email='matthias@urlichs.de',
    url='https://github.com/M-o-a-T/trio-panoramisk/',
    license='MIT license',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=test_requires,
    extras_require={
        'test': test_requires,
    },
#    entry_points='''
#    [console_scripts]
#    panoramisk = panoramisk.command:main
#    '''
)
