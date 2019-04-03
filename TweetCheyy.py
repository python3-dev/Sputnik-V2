#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:57:53 2018

@author: pratheesh
"""

import tweepy
from TwitterConf import *
#The following lines will attempt to authenticate with the OAuth credentials imported from config.py & enable the communication with Twitter
def TweetPotte(beatit):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #Create OAuth handler instance
        auth.set_access_token(access_token, access_secret) #Comment if using 0Auth dance
        api = tweepy.API(auth) #Authenticate with the API
        api.update_status(beatit) #Will update the Twitter status
        return;
    except:
        print('Twitter authentication error')
        return;