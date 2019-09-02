#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 03 20:08:00 2019

Feed Reader System for Sputnik v2 2.0
feedReader function will read the feed urls, extract the details of the latest 
ten feed entries and save it in a Python dictionary.

Input variable: feedurl
Input datatype: string
Input will be the url of a RSS feed.

Output variable: article_dict
Output datatype: dictionary
Dictionary datatype with the title of the entry as the key, and a 5 element list (feed_item_list)
containing entry author (article_author), entry link(article_link), entry summary (article_summary), 
entry published date (article_published), and published_status. Except published_status, which will
be initialised as 0, everything else including the key are string data-type.

@author: pratheesh
"""
import feedparser

def feedReader(feedurl):
    parsedfeed = feedparser.parse(feedurl)
    feed_item_list = []
    article_dict = {}
    for entrynumber in range(len(parsedfeed.entries)):
        article_title = parsedfeed.entries[entrynumber].title
        article_author = parsedfeed.entries[entrynumber].author
        article_link = parsedfeed.entries[entrynumber].link
        article_summary = parsedfeed.entries[entrynumber].summary
        article_published = parsedfeed.entries[entrynumber].published
        feed_item_list = [article_author, article_link,
                     article_summary, article_published, 0]
        article_dict[article_title] = feed_item_list
    return article_dict