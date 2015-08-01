#!/usr/bin/python
# -*- coding: utf-8 -*-

# new_config.py file is part of slpkg.

# Copyright 2014-2015 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# Slpkg is a user-friendly package manager for Slackware installations

# https://github.com/dslackw/slpkg

# Slpkg is free software: you can redistribute it and/or modify
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

from __metadata__ import MetaData as _meta_


class NewConfig(object):

    def __init__(self):
        self.meta = _meta_
        self.etc = "/etc/"
        self.news = []

    def find_new(self):
        """Find all '.new' files from /etc/ folder
        and subfolders
        """
        for path, dirs, files in os.walk("/etc/"):
            for f in files:
                if f.endswith(".new"):
                    self.news.append(os.path.join(path, f))

NewConfig().find_new()
