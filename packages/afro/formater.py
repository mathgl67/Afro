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

import string

class AbstractTransformer:
    def __init__(self, config):
        self.config = config
    def transform(self, text):
        raise NotImplementedError('call to abstract method')

class UnderscoreTransformer(AbstractTransformer):
    def transform(self, text):
        return text.replace(' ', '_')

class LowercaseTransformer(AbstractTransformer):
    def transform(self, text):
        return text.lower()

class CapwordsTransformer(AbstractTransformer):
    def transform(self, text):
        return string.capwords(text)

class ReplaceListTransformer(AbstractTransformer):
    def transform(self, text):
        for replace_from, replace_to in self.config['transformer']['replace_list'].iteritems():
            text = text.replace(replace_from, replace_to)
        return text

class RemoveListTransformer(AbstractTransformer):
    def transform(self, text):
        for remove in self.config['transformer']['remove_list']:
            text = text.replace(remove, '')
        return text

class StripTransformer(AbstractTransformer):
    def transform(self, text):
        return text.strip()

class Formater:
    __class = {
        'capwords': CapwordsTransformer,
        'underscore': UnderscoreTransformer,
        'lowercase': LowercaseTransformer,
        'replace_list': ReplaceListTransformer,
        'remove_list': RemoveListTransformer,
        'strip': StripTransformer,
    }

    def __init__(self, config):
        self.config = config
        self._inst = {}
        for name, cls in Formater.__class.iteritems():
            self._inst[name] = cls(config)

    def prepare_data(self, disc, track=None):
        data = {
            'artist': disc['artist'],
            'album': disc['title'],
            'genre': disc['genre'],
            'date': disc['date'],
            'discnumber': disc['discnumber'],
        }

        if track != None:
            data['tracknumber'] = track['tracknumber']
            data['title'] = track['title']

        return data

    def order_cmp(self, f1, f2):
        order = self.config['formater_order']

        if order.has_key(f1) and order.has_key(f2):
            return cmp(order[f1], order[f2])
        elif order.has_key(f1):
            return 1
        else:
            return -1 

    def format(self, name, disc, track=None):
        data = self.prepare_data(disc, track)
        for key in data.keys():
            text = data[key]
            # ignore non unicode data
            if not isinstance(text, int):
                transformer_list = self.config['formater'][name]['transformer']
                for transformer in sorted(transformer_list, self.order_cmp):
                    text = self._inst[transformer].transform(text)
            data[key] = text

        return self.config['formater'][name]['format'] % data

