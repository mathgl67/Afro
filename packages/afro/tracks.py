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
import mutagen

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
    result = command_run(cmd, logfile)
    
    #remove input
    if encoder['need_input_remove']:
        os.remove(infile)
        
    return result

def track_length(infile):
    audio = mutagen.File(infile, easy=True)
    return int(audio.info.length)

def track_tag(infile, track_info):
    t = mutagen.File(infile, easy=True)
    t['discnumber'] = track_info['discnumber']
    t['tracknumber'] = track_info['tracknumber']
    t['artist'] = track_info['artist']
    t['album'] = track_info['album']
    t['title'] = track_info['title']
    t['date'] = track_info['date']
    t['genre'] = track_info['genre'] 
    t.save(infile);

