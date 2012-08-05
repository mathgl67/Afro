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

import sys
import os
import codecs
import re

class M3U:
    def __init__(self, path, name, config):
        self.config = config['playlist']['m3u']
        self.file_path = u'%s.%s' % (
            os.path.join(path, name),
            self.config['extension'],
        )
        self.tracks = []

    def append(self, name, title, duration):
        self.tracks.append((name, title, duration))
        if self.config['save_on_append'] == True:
            self.save()

    def load(self):
        try:
            file_obj = codecs.open(self.file_path, 'r+', 'UTF-8')
        except IOError:
            print "[warning] hasher: cannot load file (%s)" % (self.file_path)
            return False

        state = 0
        for line in file_obj:
            line = line[:-1] 
            if state == 0:
                if line != u'#EXTM3U':
                    print '[error] file isn\'t a valid playlist (%s)' % self.file_path
                    file_obj.close()
                    sys.exit(1)
                state = state + 1
            elif state == 1:
                m = re.match(r"#EXTINF:(\d+),(.+)", line)
                duration = int(m.group(1))
                title = m.group(2)
                state = state + 1
            else:
                self.append(line, title, duration)
                state = 1

        file_obj.close()
        return True

    def save(self):
        file_obj = codecs.open(self.file_path, 'w+', 'UTF-8')
        #header
        file_obj.write(u'#EXTM3U\n')
        #tracks
        for file_name, file_title, file_duration in self.tracks:
            file_obj.write(u'#EXTINF:%d,%s\n' % (file_duration, file_title))
            file_obj.write(u'%s\n' % file_name)
        #save
        file_obj.close()

