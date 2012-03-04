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

import mutagen
import mutagen.flac
import mutagen.easyid3

from afro.utils import command_run

def track_rip(tracknumber, outfile, ripper, logfile):
    cmd = ripper['format'] % {
        'binary': ripper['binary'],
        'options': ripper['options'],
        'tracknumber': tracknumber,
        'outfile': outfile,
    }
    return command_run(cmd, logfile)

def track_enc(infile, outfile, encoder, logfile):
    cmd = encoder['format'] % {
        'binary': encoder['binary'],
        'options': encoder['options'],
        'infile': infile,
        'outfile': outfile,
    }
    return command_run(cmd, logfile)

def track_length(infile):
    audio = mutagen.flac.FLAC(infile)
    return int(audio.info.length)

def track_tag(infile, disc, track):
    tagger = []
    tagger.append(mutagen.easyid3.EasyID3())
    tagger.append(mutagen.flac.FLAC(infile))

    for t in tagger:
        t['tracknumber'] = unicode(track['tracknumber'])
        t['artist'] = disc['artist']
        t['album'] = disc['title']
        t['title'] = track['title']
        t['date'] = disc['date']
        t['genre'] = disc['genre'] 
        t.save(infile);

