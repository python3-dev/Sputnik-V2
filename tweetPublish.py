#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:57:53 2018

Tweet Publishing System for Sputnik v2 2.0

@author: pratheesh
"""

import tweepy
from twitterConf import api_key, api_secret_key, access_token, access_token_secret

def twitterPublish(message):
    try:
        auth = tweepy.OAuthHandler(api_key, api_secret_key) #Create OAuth handler instance
        auth.set_access_token(access_token, access_token_secret) #Comment if using 0Auth dance
        api = tweepy.API(auth) #Authenticate with the API
        response = api.update_status(message) #Will update the Twitter status
        return response._json
    except:
        print ('Error')