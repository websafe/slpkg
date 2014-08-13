#!/usr/bin/python
# -*- coding: utf-8 -*-

# read.py

# Copyright 2014 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# Utility for easy management packages in Slackware

# https://github.com/dslackw/slpkg

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import getpass

from slpkg.messages import s_user
from slpkg.url_read import url_read
from slpkg.__metadata__ import slpkg_path

# create tmp directory if not exist
os.system("mkdir -p {0}readme/".format(slpkg_path))

def read_readme(sbo_url, name, site):
    '''
    Read SlackBuild README file
    '''
    s_user(getpass.getuser())
    readme = url_read(sbo_url + site)
    f = open("{0}readme/{1}.{2}".format(slpkg_path, name, site), "w")
    f.write(readme)
    f.close()

def read_info_slackbuild(sbo_url, name, site):
    '''
    Read info SlackBuild file
    '''
    s_user(getpass.getuser())
    info = url_read(sbo_url + name + site)
    f = open("{0}readme/{1}{2}".format(slpkg_path, name, site), "w")
    f.write(info)
    f.close()