#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:20:18 2018

Sputnik v2 1.0

@author: pratheesh
"""

import datetime
import feedparser
import time
from unidecode import unidecode
from TweetCheyy import TweetPotte
from TwitterHandles import handleThaa
from mainConf import *


def feedReader(feedurl):
    parsedfeed = feedparser.parse(feedurl)
    feed_item = []
    article_db = {}
    for entrynumber in range(len(parsedfeed.entries)):
        article_title = parsedfeed.entries[entrynumber].title
        article_author = parsedfeed.entries[entrynumber].author
        article_link = parsedfeed.entries[entrynumber].link
        article_summary = parsedfeed.entries[entrynumber].summary
        article_published = parsedfeed.entries[entrynumber].published
        feed_item = [article_author, article_link,
                     article_summary, article_published, 0]
        article_db[article_title] = feed_item
    return article_db


def tweetComposer(title, input_dict):
    if (input_dict[title][4] == 0):
        # summary length (Max. 228) + url length (23) + username reserve (25) + spaces (1+1) + hashes (1+1)
        if (len(input_dict[title][2])+23+25+1+1+2) > 280:
            handle = handleThaa(input_dict[title][0])
            url = input_dict[title][1]
            tweet = title + handle + url  # Tweet + @author + url
        else:
            handle = handleThaa(input_dict[title][0])
            url = input_dict[title][1]
            tweet = input_dict[title][2] + \
                handle + url  # Tweet + @author + url
        return tweet
    else:
        return ' '


def printMessage(a, b, c, d, e):
    if (a > 0 and c > 0 and b > 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(a) + 'items to main_dict and ' + str(c) + ' items to tweet_dict. Removed ' +
              str(b) + ' items from main_dict & tweet_dict. The main_dict now has ' + str(d) + ' items & the tweet_dict has ' + str(e) + ' items in them.')
    elif (a > 0 and c > 0 and b == 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(a) + 'items to main_dict and ' + str(c) +
              ' items to tweet_dict. No items were removed from main_dict or tweet_dict. The main_dict now has ' + str(d) + ' items & the tweet_dict has ' + str(e) + ' items in them.')
    elif (a > 0 and c == 0 and b == 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(a) + 'items to main_dict. No items were removed from main_dict or tweet_dict. The main_dict now has ' +
              str(d) + ' items & the tweet_dict has ' + str(e) + ' items in them.')
    elif (a == 0 and c > 0 and b == 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(c) + 'items to tweet_dict. No items were removed from main_dict or tweet_dict. The main_dict now has ' +
              str(d) + ' items & the tweet_dict has ' + str(e) + ' items in them.')
    elif (a == 0 and c == 0 and b == 0):
        print(str(datetime.datetime.now()) + ': ' + 'No items were added or removed from main_dict or tweet_dict. The main_dict now has ' +
              str(d) + ' items & the tweet_dict has ' + str(e) + ' items in them.')
    elif (a == 0 and c == 0 and b > 0):
        print(str(datetime.datetime.now()) + ': ' + 'No items added to main_dict or tweet_dict. ' + str(b) +
              'items were removed from main_dict and tweet_dict. The main_dict now has ' + str(d) + ' items & the tweet_dict has ' + str(e) + ' items in them.')
    elif (a == 0 and c > 0 and b > 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(c) + 'items to tweet_dict. Removed ' + str(b) + ' items from main_dict and tweet_dict. The main_dict now has ' +
              str(d) + ' items & the tweet_dict has ' + str(e) + ' items in them.')
    elif (a > 0 and c == 0 and b > 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(a) + 'items to main_dict. Removed ' + str(b) + ' items from main_dict and tweet_dict. The main_dict now has ' +
              str(d) + ' items & the tweet_dict has ' + str(e) + ' items in them.')


main_dict = {}
tweet_dict = {}
lasttweettime = 0
lastweet = ''
starttime = time.time()

print(str(datetime.datetime.now()) + ': ' + 'Initialising...')

while(True):
    ac, arc, tc = 0, 0, 0  # For article, article removal and tweet counters

    for url in feed_dict.values():
        a = feedReader(url)
        b = main_dict.keys()
        for i in range(len(a.keys())):
            if not (a.keys()[i] in b):
                main_dict[a.keys()[i]] = (a[a.keys()[i]])
                ac += 1

    # Remove entries from the main_dict & tweet_dict only when the entry disappears from the feed items & when the item is tweeted
    for i in range(len(b)):
        if b[i] not in a.keys():
            try:
                if (tweet_dict[b[i]][1] == 1):
                    del main_dict[b[i]]
                    del tweet_dict[b[i]]
                    arc += 1
            except:
                pass

    for article_title in main_dict.keys():
        if not (article_title in tweet_dict.keys()):
            tweet_dict[article_title] = [
                tweetComposer(article_title, main_dict), 0]
            # Marking in the main_dict that tweet has been composed
            main_dict[article_title][4] = 1
            tc += 1

    printMessage(ac, arc, tc, len(main_dict.keys()), len(tweet_dict.keys()))

    for article_title in tweet_dict.keys():
        tweet = tweet_dict[article_title][0]
        if (tweet_dict[article_title][1] < 1):
            try:
                interval_condition = ((lasttweettime == 0) or (
                    (time.time()-starttime) > tweet_interval))
                not_tweeted_condition = (main_dict[article_title][4] == 1)
                not_duplicate_tweet_condition = (tweet != lastweet)
                if interval_condition and not_tweeted_condition and not_duplicate_tweet_condition:
                    TweetPotte(tweet)
                    lastweet, lasttweettime, starttime = tweet, 1, time.time()
                    main_dict[article_title][4], tweet_dict[article_title][1] = 2, 1
                    print(str(datetime.datetime.now()) +
                          ': ' + 'Published the tweet ' + tweet)
            except:
                pass
    # Sleep duration set as 600 seconds or 10 minutes or the code will search for new entries every 10 minutes
    print ('Sleeping for ' + str(refresh_interval) + ' seconds.')
    time.sleep(refresh_interval)
