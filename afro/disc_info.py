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
import tempfile 
import subprocess
import json
import musicbrainz2.disc
import musicbrainz2.webservice

def disc_info():
    service = musicbrainz2.webservice.WebService()
    query = musicbrainz2.webservice.Query(service)

    disc = musicbrainz2.disc.readDisc()
    filter = musicbrainz2.webservice.ReleaseFilter(discId=disc.getId())
    result_list = []
    for result in query.getReleases(filter):
        track_list = []
        for num, track in enumerate(result.release.tracks):
            track_list.append({
                'tracknumber': num+1,
                'title': track.title,
                'duration': track.getDuration(),
            })

        result_list.append({
            'artist': result.release.artist.name,
            'title': result.release.title,
            'date': result.release.getEarliestReleaseEvent().date,
            'genre': 'none',
            'country': result.release.getEarliestReleaseEvent().country,
            'tracks': track_list,
            
        })
    return result_list

def edit_info(disc, config):
    (file_fd, file_path) = tempfile.mkstemp() 
    file_obj = codecs.open(file_path, 'w', 'utf-8')
    json.dump(disc, file_obj, indent=2, sort_keys=True, ensure_ascii=False)
    file_obj.close()

    editor = config['tools']['editor']
    editor_options = {
        'binary': editor['binary'],
        'options': editor['options'],
        'file': file_path,
    }
    cmd = editor['format'] % editor_options
    subprocess.call(cmd.split()) 

    file_obj = codecs.open(file_path, 'r', 'utf-8')
    disc2 = json.load(file_obj)
    file_obj.close()

    return disc2

