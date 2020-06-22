#!/usr/bin/python3

CONSUMER_KEY        = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET_KEY = 'YOUR_CONSUMER_SECRET_KEY'
ACCESS_TOKEN        = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

from twitter import *

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY))

timelines = t.statuses.home_timeline()
for timeline in timelines:
    tl = '({id}) [{username}]:{text}'.format(
            id=timeline['id'], username=timeline['user']['name'], text=timeline['text'])
    print (tl)
