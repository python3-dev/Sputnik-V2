#!/usr/bin/env python3
# coding: utf-8

import datetime
import feedparser
import time

import pandas as pd

from gTools import openSheet
from telePublish import telegramPublish
from tweetPublish import twitterPublish

url_list = ["https://newsclick.in/rss.xml", "https://hindi.newsclick.in/rss.xml", "https://www.youtube.com/feeds/videos.xml?channel_id=UCOF1iS7lmNRSWVqL8N3L6kQ"] 

TESTING = False #Make sure to turn this off while in production
mention_authors = True #Whether to mention authors while tweeting.
t_sleep = 300
loop_condition = True

class Article(object):
    tag = 1
    
    def __init__(self, article_url, article_title, article_summary=None, article_author=None, article_published_time=None):
        self.url = article_url
        self.title = article_title
        self.pub_date = article_published_time
        self.articleid = Article.tag
        self.tweeted = False
        self.telegrammed = False
        Article.tag += 1

        if article_author == None:
            self.article_author = []
        else:
            self.article_author = article_author.split(',')

        if article_summary == None:
            self.article_summary = ''
        else:
            self.article_summary = article_summary
    
    def getTweetedStatus(self):
        return(self.tweeted)
    
    def setTweetedStatus(self, truth_value):
        self.tweeted = truth_value
    
    def getTelegrammedStatus(self):
        return(self.telegrammed)

    def getPublishedAllStatus(self):
        return(self.telegrammed and self.tweeted)
    
    def setTelegrammedStatus(self, truth_value):
        self.telegrammed = truth_value

    def getTitle(self):
        return(self.title)
    
    def getAuthor(self):
        return(self.article_author)    
    
    def getSummary(self):
        return(self.article_summary)
    
    def getLink(self):
        return(self.url)


class Queue(object):
    queue = {}
    
    def __init__(self, Article=None):
        if (Article != None):
            self.title = Article.getTitle()
            Queue.queue[self.title] = Article
    
    def removeItem(self,article_title):
        if article_title in Queue.queue.keys():
            del Queue.queue[article_title]
        else:
            print((f"{datetime.datetime.now()}: Failed to find the article '{article_title}'. Action removeItem() could not be completed."))
    
    def getQueue(self):
        return(list(Queue.queue.keys()))
    
    def getTelegrammedStatus(self, article_title):
        if article_title in Queue.queue.keys():
            return (Queue.queue[article_title].getTelegrammedStatus())
        else:
            print((f"{datetime.datetime.now()}: Failed to find the article '{article_title}'. Action getTelegrammedStatus() could not be completed."))
    
    def getTweetedStatus(self, article_title):
        if article_title in Queue.queue.keys():
            return (Queue.queue[article_title].getTweetedStatus())
        else:
            print((f"{datetime.datetime.now()}: Failed to find the article '{article_title}'. Action getTweetedStatus() could not be completed."))
    
    def setTweetedStatus(self, article_title):
        if article_title in Queue.queue.keys():
            Queue().getArticle(article_title).setTweetedStatus(True)
            print((f"{datetime.datetime.now()}: Set the Tweeted status of the article '{article_title}' to 'True'."))
        else:
            print((f"{datetime.datetime.now()}: Failed to find the article '{article_title}'. Action setTweetedStatus() could not be completed."))

    def setTelegrammedStatus(self, article_title):
        if article_title in Queue.queue.keys():
            Queue().getArticle(article_title).setTelegrammedStatus(True)
            print((f"{datetime.datetime.now()}: Set the Telegrammed status of the article '{article_title}' to 'True'."))
        else:
            print((f"{datetime.datetime.now()}: Failed to find the article '{article_title}'. Action setTelegrammedStatus() could not be completed."))
    
    def getPublishedAllStatus(self, article_title):
        if article_title in Queue.queue.keys():
            return (Queue.queue[article_title].getPublishedAllStatus())
        else:
            print((f"{datetime.datetime.now()}: Failed to find the article '{article_title}'. Action getPublishedAllStatus() could not be completed."))
    
    def getArticle(self, article_title):
        if article_title in Queue.queue.keys():
            return(Queue.queue[article_title])
        else:
            print((f"{datetime.datetime.now()}: Failed to find the article '{article_title}'. Action getArticle() could not be completed."))

def getAuthorHandle(author_name):
    if not(mention_authors):
        return ('')
    
    if 'newsclick' in author_name.lower():
        return('')
    else:
        try:
            return(_handles.loc[author_name, 'Twitter_Handle'])
        except:
            print(f"{datetime.datetime.now()}: Could not find '{author_name}' in the Twitter handle database.")
            return(author_name)

def makeTweet(art_obj):
    author_list = art_obj.getAuthor()
    author_handle_list = []

    for author in author_list:
        author_handle_list.append(getAuthorHandle(author))
    
    author_handle_string = ' '.join(author_handle_list)

    message = f"{art_obj.getSummary()} {author_handle_string}\n{art_obj.getLink()}"
    
    if len(message) > 280:
        message = f"{art_obj.getTitle()} {author_handle_string}\n{art_obj.getLink()}"
        if len(message) > 280:
            message = f"{art_obj.getTitle()}\n{art_obj.getLink()}"    
    
    _response = twitterPublish(message)
    print(f"{datetime.datetime.now()}: The article '{art_obj.getTitle()}' has been tweeted.")

def makeTelegram(art_obj):
    message = f"<b>{art_obj.getTitle()}</b>\n<i>{'' if len(art_obj.getSummary()) > 300 else art_obj.getSummary()}</i> \n {art_obj.getLink()}?utm_source=telg"
    _response = telegramPublish(message, TESTING)
    print(f"{datetime.datetime.now()}: The article '{art_obj.getTitle()}' has been sent over Telegram.")

def processQueue():
    for item in Queue().getQueue():
        if not(Queue().getTelegrammedStatus(item)):
            makeTelegram(Queue().getArticle(item))
            Queue().setTelegrammedStatus(item)

        if not(Queue().getTweetedStatus(item)):
            makeTweet((Queue().getArticle(item)))
            Queue().setTweetedStatus(item)
            break

def queueUpdate(feed_url):
    latest_feed = []
    feed = feedparser.parse(feed_url)
    for entry in feed['entries']:
        latest_feed.append(entry['title']) 
        if not(entry['title'] in Queue().getQueue()):
            try:
                Queue(Article(entry['link'], entry['title'], entry['summary'], entry['author'], entry['published_parsed']))
                pass
            except:
                Queue(Article(entry.get('link', None), entry.get('title', None), entry.get('summary', None),  entry.get('author'), entry.get('published_parsed', None)))
                print(f"{datetime.datetime.now()}: The RSS feed '{feed_url}' has non-compliant keys. 'None' values have been inserted. Edit the XML keys suitably for compliance.")
    return(latest_feed)

def queueClean(latest_article_list):
    for item in Queue().getQueue():
        if (not(item in latest_article_list) and Queue().getPublishedAllStatus(item)):
            Queue().removeItem(item)

def startSputnik():
    while(loop_condition):
        global _handles
        for a_url in url_list:
            latest_article_list.extend(queueUpdate(a_url))
        _handles = openSheet()
        queueClean(list(set(latest_article_list)))
        processQueue()
        if not(TESTING):
            print(f"{datetime.datetime.now()}: Sleeping for {t_sleep} seconds.")
            time.sleep(t_sleep)

if __name__ == "__main__":
    print(f"{datetime.datetime.now()}: Initialising...")
    latest_article_list = []
    _handles = openSheet()
    startSputnik()