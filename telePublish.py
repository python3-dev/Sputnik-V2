#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 3 16:13:00 2019

Telegram Publishing System for Sputnik v2 2.0

@author: pratheesh
"""

import datetime
import requests
from teleConf import apiKey, base_uri, targetChannel, testingChannel

def telegramPublish(message, testing):

    if not(testing):
        channel = targetChannel
    else:
        channel = testingChannel
    
    api_token = apiKey
    method = 'sendMessage'

    request_uri = f"{base_uri}{api_token}/{method}"

    payload =  {
        "chat_id":channel,
        "text": message,
        "parse_mode": 'HTML'
        }
    
    response = requests.post(request_uri, params = payload)

    print(f"{datetime.datetime.now()}: Successfully sent the message to the Telegram channel.")

    return(response.json())