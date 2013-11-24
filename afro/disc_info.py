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

import afro

import sys
import os
import codecs
import tempfile 
import subprocess
import json
import musicbrainzngs
import discid

def _read_disc(): 
    try:
        disc = discid.read()
    except discid.DiscError as e:
        print "[error] %s" % e.message
        sys.exit(1)
    
    return disc

def disc_sumission_url():
    disc = _read_disc()
    return disc.submission_url
    
def disc_info_cdstub(cd_stub):
    tracks = []
    for num, track in enumerate(cd_stub['track-list']):
        tracks.append({
            'tracknumber': num+1,
            'title': track['title'],
            'duration': track['length'],
        })

    return [{
        'artist': cd_stub['artist'],
        'title': cd_stub['title'],
        'date':  'none',
        'genre': 'none',
        'country': 'none',
        'tracks': tracks,
    }]

def disc_info_disc(disc):
    results = []
    for release in disc['release-list']:
        tracks = []
        for track in release['medium-list'][0]['track-list']:
            tracks.append({
                'tracknumber': track['position'],
                'title': track['recording']['title'],
                'duration': track['length'],
            })

        results.append({
            'artist': release['artist-credit'][0]['artist']['name'],
            'title': release['title'],
            'date':  release['date'],
            'genre': 'none',
            'country': release['country'],
            'tracks': tracks,
        })

    return results

def disc_info_fetch(disc_id=None):
    if not disc_id:
        disc = _read_disc()
        disc_id = disc.id

    musicbrainzngs.set_useragent(afro.name, afro.version, afro.url)
    try:
        return musicbrainzngs.get_releases_by_discid(disc_id, includes=['artists', 'recordings'])
    except musicbrainzngs.ResponseError as exception:
        return None

def disc_info(disc_id=None):
    fetched = disc_info_fetch(disc_id)

    if 'disc' in fetched:
        return disc_info_disc(fetched['disc'])
    elif 'cdstub' in fetched:
        # If not official musicbrainz data found we can fetch a cdstub...
        return disc_info_cdstub(fetched['cdstub'])
    else:
        print json.dumps(fetched, indent=2)
        sys.exit(1)

def edit_info(disc, config):
    (file_fd, file_path) = tempfile.mkstemp()
    os.close(file_fd)
    
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

