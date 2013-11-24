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

from unittest import TestCase

from afro.disc_info import disc_info_fetch, disc_info_cdstub, disc_info_disc

class DiscInfoTestCase(TestCase):
    def test_unknow_id(self):
        fetched = disc_info_fetch(u'-4-4-4-4-4-4-4-4-4-4-4-44-4-')
        self.assertIsNone(fetched)

    def test_cdstub(self):
        fetched = disc_info_fetch(u'T6s7QfXlANjjSGyxSYob0cVy1w8-')
        releases = disc_info_cdstub(fetched['cdstub'])

        self.maxDiff = None
        self.assertEqual(len(releases), 1)
        self.assertEqual(releases[0], {
            'artist': u'Détroit',
            'title': 'Horizon',
            'date': 'none',
            'country': 'none',
            'genre': 'none',
            'tracks': [
                {'duration': '302640', 'tracknumber': 1, 'title': 'Ma muse'},
                {'duration': '305933', 'tracknumber': 2, 'title': 'Glimmer in your Eyes'},
                {'duration': '210573', 'tracknumber': 3, 'title': u'Terre brûlante'},
                {'duration': '90053', 'tracknumber': 4, 'title': u'Détroit - 1'},
                {'duration': '235866', 'tracknumber': 5, 'title': u'Ange de désolation'},
                {'duration': '303320', 'tracknumber': 6, 'title': 'Horizon'},
                {'duration': '204746', 'tracknumber': 7, 'title': 'Droit dans le soleil'},
                {'duration': '36960', 'tracknumber': 8, 'title': u'Détroit - 2'},
                {'duration': '221226', 'tracknumber': 9, 'title': 'Le creux de ta main'},
                {'duration': '263053', 'tracknumber': 10, 'title': u'Sa majesté'},
                {'duration': '275506', 'tracknumber': 11, 'title': 'Null and Void'},
                {'duration': '265413', 'tracknumber': 12, 'title': 'Avec le temps'},
                {'duration': '442720', 'tracknumber': 13, 'title': '[untitled]'}
            ]
        })

    def test_disc(self):
        fetched = disc_info_fetch(u'm3brZc1VmwFJLzHQx9RJ0KezFHc-')
        releases = disc_info_disc(fetched['disc'])

        self.maxDiff = None
        self.assertTrue(len(releases) >= 1)
        self.assertEqual(releases[0], {
            'artist': 'The Doors',
            'title': 'Waiting for the Sun',
            'date': '2007-03-27',
            'country': 'US',
            'genre': 'none',
            'tracks': [
                {'duration': '160453', 'tracknumber': '1', 'title': 'Hello, I Love You'},
                {'duration': '176813', 'tracknumber': '2', 'title': 'Love Street'},
                {'duration': '240506', 'tracknumber': '3', 'title': 'Not to Touch the Earth'},
                {'duration': '202960', 'tracknumber': '4', 'title': u'Summer\u2019s Almost Gone'},
                {'duration': '116600', 'tracknumber': '5', 'title': 'Wintertime Love'},
                {'duration': '206960', 'tracknumber': '6', 'title': 'The Unknown Soldier'},
                {'duration': '182480', 'tracknumber': '7', 'title': 'Spanish Caravan'},
                {'duration': '181093', 'tracknumber': '8', 'title': 'My Wild Love'},
                {'duration': '143760', 'tracknumber': '9', 'title': 'We Could Be So Good Together'},
                {'duration': '162426', 'tracknumber': '10', 'title': 'Yes, the River Knows'},
                {'duration': '273466', 'tracknumber': '11', 'title': 'Five to One'},
                {'duration': '272466', 'tracknumber': '12', 'title': u'Albinoni\u2019s Adagio in G Minor'},
                {'duration': '43453', 'tracknumber': '13', 'title': 'Not to Touch the Earth (dialogue)'},
                {'duration': '239493', 'tracknumber': '14', 'title': 'Not to Touch the Earth (take 1)'},
                {'duration': '257640', 'tracknumber': '15', 'title': 'Not to Touch the Earth (take 2)'},
                {'duration': '1029440', 'tracknumber': '16', 'title': 'Celebration of the Lizard (An Experiment/Work in Progress)'}
            ]
        })
