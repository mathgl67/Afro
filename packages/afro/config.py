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

import codecs
import os.path

import yaml
try:
    from yaml import CLoader as yamlLoader
except ImportError:
    from yaml import Loader as yamlLoader


class ConfigStore(dict):
    def load(self, name):
        raise Exception("this is an abstract method")

    def _load_file_list(self, file_list):
        for filepath in file_list:
            self._update(self._read_file(filepath))

    def _update(self, data):
        Config._update_real(self, data)

    @staticmethod
    def _update_real(item, data):
        for key, value in data.iteritems():
            if isinstance(value, dict):
                if not item.has_key(key) or not isinstance(item[key], dict):
                    item[key] = {}
                Config._update_real(item[key], value)
            else:
                item[key] = value

    def _read_file(self, filepath):
        data = {}
        try:
            with codecs.open(filepath, 'r', 'utf-8') as f:
                data = yaml.load(f, Loader=yamlLoader)
        except Exception:
            print "[warning] config: file '%s' could not be loaded" % (filepath)

        return data
   
class Config(ConfigStore):
    def load(self, filepath=None):
        file_list = [
            os.path.join(os.path.dirname(__file__), u'config.default.yml'),
            os.path.expanduser(os.path.join(u'~', u'.config', u'afro', u'config.yml')),
        ]

        if (filepath):
            file_list.append(filepath)

        self._load_file_list(file_list)

    def get_profile(self, name=None):
        profile = Profile()
        profile.load(name if name else self['profile'])
        return profile

class Profile(ConfigStore):
    def load(self, name):
        file_list = [
            os.path.join(os.path.dirname(__file__), u'profiles', u'default.yml'),
            os.path.join(os.path.dirname(__file__), u'profiles', u'%s.yml' % name),
            os.path.expanduser(os.path.join(u'~', u'.config', u'afro', u'profiles', u'%s.yml' % name)),
        ]

        self._load_file_list(file_list)

