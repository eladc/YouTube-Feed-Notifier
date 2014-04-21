#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ytnotifications.py - pop up notifications about new videos 
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

import pynotify
import gobject
from time import sleep
from webbrowser import open as webopen

def OnClicked(notification, signal_text):
    webopen(ytUrl)
    notification.close()
    global loop
    loop.quit()

def OnClosed(notification):
    notification.close()
    global loop
    loop.quit()

def mainNotify(uploader, title, dur, url):
    global ytUrl # a global var to be passed to web browser
    ytUrl = url
    upload = 'New video from ' + uploader
    titledur = title + '  ' +'['+dur+']'
    pynotify.init('YouTube Feed Notifier')

    global loop
    loop = gobject.MainLoop()
    notify = pynotify.Notification(upload, titledur ,'/usr/share/pixmaps/youtube.png')

    notify.set_urgency(pynotify.URGENCY_LOW)

    notify.set_timeout(pynotify.EXPIRES_NEVER)

    notify.add_action('text', 'View on YouTube', OnClicked)
    notify.connect("closed",OnClosed)
    
    notify.show()

    loop.run()

