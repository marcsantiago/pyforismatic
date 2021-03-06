﻿#!/usr/bin/python

from distutils.core import setup

setup(name='forismatic',
      version='1.0',
      description='PyForismatic package',
      long_description = "Getting quotes from http://forismatic.com using API",
      author='Marc Santiago',
      author_email='marcanthonysanti@gmail.com',
      url='marcsantiago.com',
      packages=['forismatic'],
      scripts=['example.py'],

      classifiers=(
          'Development Status :: 5 - Production/Stable',
          'Environment :: Plugins',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
        ),
      license="GPL-2"
     )
