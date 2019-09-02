#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 03 20:08:00 2019

Sputnik v2 1.0
Message construction system for Sputnik V2

messageComposer function will create messages that needs to be sent to Twitter or Telegram, from the article details. 
The function will have three inputs: ttl, input_dict, t0
ttl: String datatype. Title of the article.
input_dict: Dictionary datatype. Every key (which is ttl) is mapped to a 5 element list. The list contains further details
of the article.
t0: Either 0 or 1. Defines the context of making the message. 0 corresponds to Twitter, and 1 corresponds to Telegram.

Function returns a 2 element tuple - with twitter message and telegram message - when 


@author: pratheesh
"""
from twitterHandles import handleThaa

def messageComposer(ttl, input_dict,t0):
    title = ttl 
    url = input_dict[title][1]
    summary = input_dict[title][2]
    t = t0
    if t == 1:
        if (input_dict[title][4] == 0):
            handle = handleThaa(input_dict[title][0])
            # summary length (Max. 228) + url length (23) + username reserve (25) + spaces (1+1) + hashes (1+1)
            if (len(summary)+23+25+1+1+2) > 280:
                message = title + handle + url  # Tweet + @author + url
            else:
                message = summary + handle + url  # Tweet + @author + url
            return message

    elif t == 2:
        if (input_dict[title][4] == 0):
            message = "<b>" + summary + "</b> \n" + url 
            return message