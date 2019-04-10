#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:20:18 2018

Sputnik 0.2



@author: pratheesh
"""

import datetime
import feedparser
import time
from unidecode import unidecode
from TweetCheyy import TweetPotte
from TwitterHandles import handleThaa
from mainConf import *

def feedReader (feedurl):
    parsedfeed = feedparser.parse(feedurl)
    feed_item = []
    article_db = {}
    for entrynumber in range(len(parsedfeed.entries)):
        article_title = parsedfeed.entries[entrynumber].title
        article_author = parsedfeed.entries[entrynumber].author
        article_link = parsedfeed.entries[entrynumber].link
        article_summary = parsedfeed.entries[entrynumber].summary
        article_published = parsedfeed.entries[entrynumber].published
        feed_item = [article_author, article_link, article_summary, article_published,0]
        article_db[article_title] = feed_item
    return article_db

def tweetComposer(title, input_dict):
    if (input_dict[title][4] == 0):
        if (len(input_dict[title][2])+23+25+1+1+2) > 280: # summary length (Max. 228) + url length (23) + username reserve (25) + spaces (1+1) + hashes (1+1)
            handle = handleThaa(input_dict[title][0])
            url = input_dict[title][1]
            tweet = title + ' ' + handle + ' ' + url  # Tweet + @author + url
        else:
            handle = handleThaa(input_dict[title][0])
            url = input_dict[title][1]
            tweet = input_dict[title][2] + ' ' + handle + ' ' + url  # Tweet-author-url
        return tweet
    else:
        return ' '


main_dict = {}
tweet_dict = {}
lasttweettime = 0
starttime = time.time()

print(str(datetime.datetime.now()) + ': ' + 'Initialising...')

while(True):
    for url in feed_dict.values():
        a = feedReader(url)
        b = main_dict.keys()
        for i in range(len(a.keys())):
            if not (a.keys()[i] in b):
                main_dict[a.keys()[i]] = (a[a.keys()[i]])
    print str(datetime.datetime.now()) + ': ' + 'Main article database have ' + str(len(main_dict.keys())) + 'articles now.'

    if (len(tweet_dict.keys()) > 15*len(feed_dict.keys())):
        for article_title in main_dict.keys(): #Remove entries if the tweeet is already published
            try:
                if (tweet_dict[article_title][1] == 1):
                    del main_dict[article_title]
            except:
                pass
        print(str(datetime.datetime.now()) + ': ' + 'Cleaned the main article database')

    for article_title in main_dict.keys():
        if not (article_title in tweet_dict.keys()):
            tweet_dict[article_title] = [tweetComposer(article_title, main_dict),0]
            main_dict[article_title][4] = 1 #Marking that tweet has been composed
    print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(len(tweet_dict.keys())) + ' tweets added to Tweet database')
    
    if (len(tweet_dict.keys()) > 15*len(feed_dict.keys())):
        for article_title in tweet_dict.keys(): #Remove entries if the tweeet is already published
            if (tweet_dict[article_title][1] == 1):
                del tweet_dict[article_title]
        print(str(datetime.datetime.now()) + ': ' + 'Cleaned the tweet database')

    for article_title in tweet_dict.keys():
        tweet = tweet_dict[article_title][0]
        if (tweet_dict[article_title][1] < 1):
            try:
                if ((main_dict[article_title][4] == 1) and (lasttweettime == 0)):
                    TweetPotte(tweet)
                    lasttweettime = 1
                    starttime = time.time()
                    main_dict[article_title][4], tweet_dict[article_title][1] = 2, 1
                    print(str(datetime.datetime.now()) + ': ' + 'Published the tweet ' + tweet)
                elif ((main_dict[article_title][4] == 1) and ((time.time()-starttime) > tweet_interval)):
                    TweetPotte(tweet)
                    lasttweettime = 1
                    starttime = time.time()
                    main_dict[article_title][4], tweet_dict[article_title][1] = 2, 1
                    print(str(datetime.datetime.now()) + ': ' + 'Published the tweet ' + tweet)
            except:
                pass
    # Sleep duration set as 600 seconds or 10 minutes or the code will search for new entries every 10 minutes
    time.sleep(refresh_interval)
