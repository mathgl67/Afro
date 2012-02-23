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

import os
import codecs

class M3U:
    def __init__(self, path, name, config):
        self.config = config['playlist']['m3u']
        self.path = path
        self.name = name
        self.tracks = []

    def append(self, filename, track):
        self.tracks.append((filename, track))
        if self.config['save_on_append'] == True:
            self.save()

    def save(self):
        file_obj = codecs.open(u'%s.%s' % (
                os.path.join(self.path, self.name),
                self.config['extension']
            ),
            'w+', 'UTF-8'
        )
        #header
        file_obj.write(u'#EXTM3U\n')
        #tracks
        for file_name, track in self.tracks:
            file_obj.write(u'#EXTINF:%d,%s\n' % (track['duration']/1000, track['title']))
            file_obj.write(u'%s\n' % file_name)
        #save
        file_obj.close()

           

