#!/usr/bin/env python3
# coding: utf-8

import datetime
import pygsheets

import pandas as pd

key_path = "key_google_spreadsheet.json" #Key to JSON file for authenticating pygsheets with the Google Sheets API
destination_spreadsheet_url = "" #direct url to spreadsheet. Follow pygsheets documentation: https://pygsheets.readthedocs.io/en/stable/

gc = pygsheets.authorize(service_file=key_path)
sh = gc.open_by_url(destination_spreadsheet_url)

def googleWrite(dictionary, prefix_string = "", sh = sh):
    """
    Writes dataframes stored as dictionary values as Google spreadsheets
    
    Parameters:
    dictionary (dict): Python dictionary which has values as corresponding dataframes and keys to identify them
    prefix_string (str): prefix-string for worksheet name, defaults to a zero-length string
    
    Returns:
    Nothing
    
    """
    
    for key, value in dictionary.items():
        sheet_title = prefix_string + key
        try:
            wks = sh.worksheet_by_title(sheet_title)
        except:
            print(f"{datetime.datetime.now()}: Could not find {sheet_title}.")
            continue
        df = value.copy()
        wks.set_dataframe(df,'A1', copy_index=True)
        print(f"{datetime.datetime.now()}: Finished writing {sheet_title}.")



def openSheet(worksheet_title=None, sh = sh):
    if worksheet_title == None:
        df = sh.sheet1.get_as_df()[['Author_Name', 'Twitter_Handle']].set_index('Author_Name')
        return(df)
    
    else:
        ws = sh.worksheet_by_title(worksheet_title)
        df = ws.get_as_df()
        df.set_index(df.columns[0], inplace = True, drop = True)
        return(df)

