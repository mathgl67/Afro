#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:set ts=4 sw=4 expandtab:
#
# AFRO
# Copyright (C) 2011-2012 mathgl67
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup
from pip.req import parse_requirements

def requirements(file_name):
    requirements = parse_requirements(file_name)
    return [str(requirement.req) for requirement in requirements]

setup(
    name='afro',
    author='mathgl67',
    author_email='mathgl67_AT_gmail.com',
    version='0.5.5',
    description='Another Free Ripping Orchestra',
    long_description=open('README.rst').read(),
    url='https://github.com/mathgl67/Afro',
    packages=['afro'],
    package_dir={'afro': 'packages/afro'},
    package_data={'afro': ['config.default.yaml']},
    scripts=['scripts/afro'],
    download_url='https://github.com/mathgl67/Afro/releases',
    platforms=['Linux', 'MacOSx'],
    license=open('COPYING.txt').read(),
    install_requires=requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Ripping',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
    ]
)

