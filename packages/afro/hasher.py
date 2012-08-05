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
import os
import zlib
import hashlib 
import re

class AbstractHasher:
    def __init__(self, path, name, config):
        self.path = path
        self.name = name
        self.results = {}
        self.set_config(config)
        # prepare file full path
        self.file_fullpath = os.path.join(self.path, '%(file)s.%(extension)s' % {
            'file': self.name,
            'extension': self.config['extension'],
        })
    
    def set_config(self, config):
        raise NotImplementedError('call to abstract method')

    def perform_hash(self, file_obj):
        raise NotImplementedError('call to abstract method')

    def perform(self, file_name):
        fullpath = os.path.join(self.path, file_name)
        file_obj = open(fullpath, 'rb')
        self.results[file_name] = self.perform_hash(file_obj) 
        file_obj.close()

    def save_write_result(self, file_obj, result):
        raise NotImplementedError('call to abstract method')

    def load_line(self, line):
        raise NotImplementedError('call to abstract method')

    def load(self):
        try:
            file_obj = codecs.open(self.file_fullpath, "r+", "utf-8")
        except IOError:
            print "[warning] hasher: cannot load file (%s)" % (self.file_fullpath)
            return False
        
        for line in file_obj:
            self.load_line(line)
        file_obj.close()

    def save(self):
        file_obj = codecs.open(self.file_fullpath, "w+", "utf-8")
        for key in sorted(self.results.keys()):
            self.save_write_result(file_obj, {
                'file_name': key,
                'file_hash': self.results[key],
            })
        file_obj.close()

       

class SFV(AbstractHasher):
    def set_config(self, config):
        self.config = config['hasher']['sfv']
    
    def perform_hash(self, file_obj):
        return '%08x' % (zlib.crc32(file_obj.read()) & 0xffffffff)

    def load_line(self, line):
        #ignore comment
        if re.search(r"^[;#]+", line):
            return

        m=re.match(r"^(.+) (\S+)$", line)
        self.results[m.group(1)] = m.group(2)

    def save_write_result(self, file_obj, result):
        file_obj.write(u'%(file_name)s %(file_hash)s\n' % (result))
        
class Shasum(AbstractHasher):
    def set_config(self, config):
        self.config = config['hasher']['shasum']

    def perform_hash(self, file_obj):
        hasher = hashlib.new(self.config['algorithm'])
        hasher.update(file_obj.read())
        return hasher.hexdigest()

    def load_line(self, line):
        #ignore comment
        if re.search(r"^[;#]+", line):
            return

        m=re.match(r"^(\S+)  (.+)$", line)
        self.results[m.group(2)] = m.group(1)

    def save_write_result(self, file_obj, result):
        #must have two space as separator
        file_obj.write(u'%(file_hash)s  %(file_name)s\n' % result)
        

class Hasher:
    __class = {
        'sfv': SFV,
        'shasum': Shasum,
    }

    def __init__(self, path, name, config):
        self.config = config['hasher']
        self.hasher_obj = []
        for hasher_name in config['hasher']['list']:
            self.hasher_obj.append(Hasher.__class[hasher_name](path, name, config))

    def perform(self, file_name):
        for hasher in self.hasher_obj:
            hasher.perform(file_name)
        
        if self.config['save_on_perform'] == True:
            self.save()

    def load(self):
        for hasher in self.hasher_obj:
            hasher.load()

    def save(self):
        for hasher in self.hasher_obj:
            hasher.save()

