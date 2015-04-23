#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DIR = os.path.dirname(os.path.abspath(__file__))

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

version = '1.0.0'


setup(
    name='whatswhere',
    version=version,
    description="Find out where you can test the functionality of a pull request.",
    author='Piper Merriam',
    author_email='piper@simpleenergy.com',
    url='https://github.com/simpleenergy/whatswhere',
    include_package_data=True,
    py_modules=['whatswhere'],
    install_requires=[
        "PyGithub==1.25.2",
        "GitPython==1.0.0",
        "requests==2.6.0",
        "npyscreen==4.8.6",
    ],
    license="BSD",
    zip_safe=False,
    entry_points={
        'console_scripts': ["ww=whatswhere.cli:main"],
    },
    keywords='murr',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
