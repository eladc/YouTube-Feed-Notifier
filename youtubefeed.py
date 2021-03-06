#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# YouTubeFeed.py - A module to get new videos from a user's subscriptions
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

import requests
from json import loads
from time import gmtime, strftime

class YouTubeFeed:
  def __init__(self, username):
    self.username = username

  def getFeed(self):
    ## get a subscription feed from YT:
    self.resp = requests.get('https://gdata.youtube.com/feeds/api/users/%s/newsubscriptionvideos?v=2&alt=jsonc' % self.username) 
    if(self.resp.status_code == 200):
      data = loads(self.resp.content)
      return data
    else:
      print "There was an error..." ## these lines probably need a rewrite
      return 0 ##

  def firstFeedUpdate(self):
    videos = []
    for item in self.getFeed()['data']['items']:
      videos.append(item['id'])
    return videos
 
  def feedUpdate(self, old_videos): # call this funcion in a timed loop to check for new videos
    fullfeed = {} # full details about new videos to be passed to notifier
    n = 0
    data = self.getFeed()
    for item in data['data']['items']:
      if item['id'] not in old_videos:
        vid_time = strftime('%M:%S', gmtime(item['duration']))
        fullfeed[n] = [item['uploader'], item['title'], vid_time, item['player']['default'], item['thumbnail']['sqDefault']]
        old_videos.insert(0, item['id']) # insert new object to first index
        old_videos.pop(-1) # remove last object
        n += 1
    return old_videos, fullfeed # returns a dictionary of newly uploaded videos

