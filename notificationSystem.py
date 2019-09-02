#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 03 20:08:00 2019

Message Notification System for Sputnik v2 2.0

@author: pratheesh
"""
import datetime

def printMessage(a, b, c, d, e):
    if (a > 0 and c > 0 and b > 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(a) + ' items to main_dict and ' + str(c) + ' items to message_dict. Removed ' +
              str(b) + ' items from main_dict & message_dict. The main_dict now has ' + str(d) + ' items & the message_dict has ' + str(e) + ' items in them.')
    elif (a > 0 and c > 0 and b == 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(a) + ' items to main_dict and ' + str(c) +
              ' items to message_dict. No items were removed from main_dict or message_dict. The main_dict now has ' + str(d) + ' items & the message_dict has ' + str(e) + ' items in them.')
    elif (a > 0 and c == 0 and b == 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(a) + ' items to main_dict. No items were removed from main_dict or message_dict. The main_dict now has ' +
              str(d) + ' items & the message_dict has ' + str(e) + ' items in them.')
    elif (a == 0 and c > 0 and b == 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(c) + ' items to message_dict. No items were removed from main_dict or message_dict. The main_dict now has ' +
              str(d) + ' items & the message_dict has ' + str(e) + ' items in them.')
    elif (a == 0 and c == 0 and b == 0):
        print(str(datetime.datetime.now()) + ': ' + 'No items were added or removed from main_dict or message_dict. The main_dict now has ' +
              str(d) + ' items & the message_dict has ' + str(e) + ' items in them.')
    elif (a == 0 and c == 0 and b > 0):
        print(str(datetime.datetime.now()) + ': ' + 'No items added to main_dict or message_dict. ' + str(b) +
              'items were removed from main_dict and message_dict. The main_dict now has ' + str(d) + ' items & the message_dict has ' + str(e) + ' items in them.')
    elif (a == 0 and c > 0 and b > 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(c) + 'items to message_dict. Removed ' + str(b) + ' items from main_dict and message_dict. The main_dict now has ' +
              str(d) + ' items & the message_dict has ' + str(e) + ' items in them.')
    elif (a > 0 and c == 0 and b > 0):
        print(str(datetime.datetime.now()) + ': ' + 'Added ' + str(a) + 'items to main_dict. Removed ' + str(b) + ' items from main_dict and message_dict. The main_dict now has ' +
              str(d) + ' items & the message_dict has ' + str(e) + ' items in them.')