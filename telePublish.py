#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 3 16:13:00 2019

Telegram Publishing System for Sputnik v2 2.0

@author: pratheesh
"""

import requests
from teleConf import *

def telegramPublish(message):
    global apiKey
    global targetChannel
    global base_uri
    api_token = apiKey
    method = 'sendMessage'

    request_uri = base_uri + api_token + '/' + method

    payload =  {
        "chat_id":targetChannel,
        "text": message,
        "parse_mode": 'HTML'
        }
    
    response = requests.post(request_uri, params = payload)
    return(response.json())