#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:20:18 2018

Sputnik v2 2.0

@author: pratheesh
"""

import datetime
import time
from unidecode import unidecode
from tweetCheyy import TweetPotte
from feedVaayikku import feedReader
from messageOndaakku import messageComposer
from notificationSystem import printMessage
from telePublish import telegramPublish
from mainConf import *

main_dict = {}
message_dict = {}
lastmessagetime = 0
lastmessage = ''
starttime = time.time()

print(str(datetime.datetime.now()) + ': ' + 'Initialising...')

while(True):
    ac, arc, tc = 0, 0, 0  # For article, article removal and tweet counters
    c = [] #Latest list of articles from multiple feeds

    for url in feed_dict.values(): #feed_dict, which is the dictionary of feeds is imported from mainConf.py
        a = feedReader(url)
        b = main_dict.keys()
        for i in a.iterkeys():
            c.append(i)
            if not (i in b):
                main_dict[i] = a[i] #Add an element to the main_dict, if it does not exist in main_dict
                ac += 1 #Count the number of additions to main_dict during an iteration

    for i in main_dict.iterkeys(): # Remove entries from the main_dict & tweet_dict only when the entry disappears from the feed items & when the item is tweeted
        if not (i in c): #if an article_title in the dictionary is not found in the latest list of articles from the feeds
            try:
                if (message_dict[i][4] == 1): #try to see if the article is queued to be tweeted
                    del main_dict[i]
                    del message_dict[i]
                    arc += 1
            except:
                pass

    for article_title in main_dict.keys():
        if not (article_title in message_dict.keys()):
            message_dict[article_title] = [
                messageComposer(article_title, main_dict, 1), messageComposer(article_title, main_dict, 0), 0]
            main_dict[article_title][4] = 1 # Marking in the main_dict that tweet has been composed
            tc += 1

    printMessage(ac, arc, tc, len(main_dict.keys()), len(message_dict.keys()))

    for article_title in message_dict.keys():
        tweet_message = message_dict[article_title][0]
        tele_message = message_dict[article_title][1]
        if (message_dict[article_title][2] < 1):
            try:
                interval_condition = ((lastmessagetime == 0) or (
                    (time.time()-starttime) > tweet_interval))
                not_tweeted_condition = (main_dict[article_title][4] == 1)
                not_duplicate_tweet_condition = (tweet_message != lastmessage)
                if interval_condition and not_tweeted_condition and not_duplicate_tweet_condition:
                    TweetPotte(tweet_message)
                    tele_response = telegramPublish(tele_message)
                    lastmessage, lastmessagetime, starttime = tweet_message, 1, time.time()
                    main_dict[article_title][4], message_dict[article_title][2] = 2, 1
                    print(str(datetime.datetime.now()) +
                          ': ' + 'Transmitted a message ~ [' + tweet_message + ']')
            except:
                print(str(datetime.datetime.now()) + ': ' +
                      'Failed to transmit the message ~ [' + tweet_message + ']')
    # Sleep duration set as 600 seconds or 10 minutes or the code will search for new entries every 10 minutes
    print (str(datetime.datetime.now()) + ': Sleeping for ' +
           str(refresh_interval) + ' seconds.')
    time.sleep(refresh_interval)
