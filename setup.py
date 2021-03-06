#!/usr/bin/env python

import os
import sys
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name="rst2ansi",
  version="0.1.5",
  author="Snaipe",
  author_email="franklinmathieu@gmail.com",
  description="A rst converter to ansi-decorated console output",
  long_description=read('README.rst'),
  license="MIT",
  keywords="rst restructuredtext ansi console code converter",
  url="https://github.com/Snaipe/python-rst-to-ansi",
  packages=['rst2ansi'],
  install_requires=['docutils'],
  entry_points = {
    'console_scripts': ['rst2ansi=rst2ansi.__main__:main'],
  },
  data_files=[],
  classifiers=[
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Text Processing :: Markup",
    "Topic :: Utilities",
  ],
)
