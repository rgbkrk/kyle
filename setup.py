#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version="0.0.3"

if sys.argv[-1] == 'publish':
    print("Publishing Kyle {version}".format(version=version))
    os.system('python setup.py sdist upload')
    sys.exit()

packages = ['kyle']
requires = []

#with open('requirements.txt') as reqs:
#    requires = reqs.read().splitlines()

setup(name='kyle',
      version=version,
      description='Kyle the Python module',
      author='Kyle Kelley',
      author_email='rgbkrk@gmail.com',
      url='http://github.com/rgbkrk/kyle',
      packages=packages,
      package_data={'': ['LICENSE']},
      include_package_data=False,
      install_requires=requires,
      license=open('LICENSE').read(),
      zip_safe=False,
      classifiers=(
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7'
      ),
)
