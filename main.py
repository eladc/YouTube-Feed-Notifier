#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
#
#
# Elad Cohen <eladco@gmail.com>
##########################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
##########################################

import youtubefeed as yt
import threading
import gobject
from sys import argv
from time import sleep
from ytnotifications import *

'''
Feed structure example:
##############
{0: [u'uploader', u'title', 'duration', u'url']}
##############
'''
def main(user):
    feedObj = yt.YouTubeFeed(user) # create an instance of Youtube Feed
    feedIds = feedObj.firstFeedUpdate() # get the initial feed
    while True:
        feedIds, feedData = feedObj.feedUpdate(feedIds)  # check for new feeds
        if len(feedData) > 0 :  
            for key in feedData:
                uploader = feedData[key][0]
                title = feedData[key][1]
                dur = feedData[key][2]
                url = feedData[key][3]
                threading.Thread(target=mainNotify(uploader, title, dur, url)).start() # send new feed to notifications
        sleep(900)

if __name__ == '__main__':
    gobject.threads_init()
    t = threading.Thread(target=main(argv[1]))
    t.daemon = True
    t.start()
    gobject.MainLoop().run()

