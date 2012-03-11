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
import argparse

from afro.config import Config
from afro.disc_info import disc_info, edit_info 
from afro.formater import Formater
from afro.hasher import Hasher
from afro.playlist import M3U
from afro.tracks import track_rip, track_enc, track_tag, track_length

class Application:
    def list(self, args):
        num = 0
        infos = disc_info()
        for disc in infos:
            num = num + 1
            disc['num'] = num 
            print '%(num)d - %(artist)s - %(title)s - %(date)s - %(country)s' % disc 

    def info(self, args):
        infos = disc_info()
        info = infos[args.num - 1]

        for track in info['tracks']:
            print '%(tracknumber)s - %(title)s - %(duration)s' % track
        
        
    def rip(self, args):
        # read config
        config = Config()
        config.load(args.config)

        #get profile
        profile = config.get_profile(args.profile)

        # read disc info
        di = disc_info()
        disc = di[args.num - 1]

        # edit
        if args.edit:
            disc = edit_info(disc, config)

        # prepare disc
        if args.genre:
            disc['genre'] = args.genre

        # prepare the formater
        formater = Formater(profile)

        # prepare folder
        folder_name = formater.format('folder', disc) 
        folder = os.path.join(config['output']['basedir'], folder_name)

        try:
            os.makedirs(folder)
        except OSError:
            print "Directory already exists or permission denied"

        #metafiles
        ff = formater.format('metafiles', disc)

        #prepare hash
        hasher = Hasher(folder, ff, profile)

        #prepare playlist
        m3u = M3U(folder, ff, profile)

        #track jobs.
        for track in disc['tracks']:
            track_name = formater.format('track', disc, track) 
            track_path = u'%s/%s' % (folder, track_name)
            track_ext = profile['tools']['encoder']['extension']
            track_out = u'%s.%s' % (track_path, track_ext)
            track_wav = u'%s.wav' % (track_path)
            
            track_info = {
              'date': disc['date'],
              'tracknumber': unicode(track['tracknumber']),
              'title': track['title'],
              'album': disc['title'],
              'artist': disc['artist'],
              'genre': disc['genre'],
            }

            #rip
            print 'rip:', track_name
            track_rip(track['tracknumber'], track_wav, profile['tools']['ripper'], config['logging'])

            #encode
            print 'encode:', track_name
            track_enc(track_wav, track_out, profile['tools']['encoder'], config['logging'])
        
            #tags
            print 'tag:', track_name
            track_tag(track_out, track_info)
    
            #get the real track length
            track['duration_real'] = track_length(track_out)
       
            #perform hash on the file
            hasher.perform(u'%s.%s' % (track_name, track_ext))
        
            #playlist
            m3u.append(u'%s.%s' % (track_name, track_ext), track)

        #save hash
        hasher.save()
    
        #save playlist
        m3u.save()

    def main(self):
        # args parser
        parser = argparse.ArgumentParser(description="Another Flac Ripping Ohohoh")
        subparsers = parser.add_subparsers(title="commands", description="valid command")

        parser_list = subparsers.add_parser('list')
        parser_list.set_defaults(func=self.list)

        parser_info = subparsers.add_parser('info')
        parser_info.set_defaults(func=self.info)
        parser_info.add_argument('num', type=int)

        parser_rip = subparsers.add_parser('rip')
        parser_rip.set_defaults(func=self.rip)
        parser_rip.add_argument('--genre')
        parser_rip.add_argument('--edit', '-e', action="store_true")
        parser_rip.add_argument('--config', '-c')
        parser_rip.add_argument('--profile', '-p')
        parser_rip.add_argument('num', type=int)

        args = parser.parse_args()
        args.func(args)
 
