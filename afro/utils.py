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
import subprocess

def command_run(command, logging):
    logger=None
    if logging['enable']:
        logger = codecs.open(logging['file'], 'w+', 'utf-8')
        logger.write(u'command_run: %s\n' % (command))
    
    command_array = command.split(' ')
    command_retcode = subprocess.call(command_array, stdout=logger, stderr=logger)
    return command_retcode == 0

