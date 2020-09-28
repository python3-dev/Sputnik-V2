#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 03:57:59 2019

Twitter Handles Reader System for Sputnik v2 2.0

@author: pratheesh
"""

import csv

def handleThaa(name):
    tweepdict = {}
    for row in csv.reader(open('handles.csv')):
        tweepdict[row[0].strip()]= row[1].strip()
    if (tweepdict.has_key(name)):
        return (' ' + tweepdict[name] + ' ')
    else:
        return ' '