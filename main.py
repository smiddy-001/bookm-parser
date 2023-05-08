#!/usr/bin/env python3

                        # This is a script designed to pull rip and reorganise and reformat html,
                        # json and other wierd configs of bookmarks, turn them into csv format and 
                        # use that csv in a local hoseted webpage and use that webpage as a quicklink 
                        # bookmarks new tab.

## Imports
import csv
from bs4 import BeautifulSoup

## Config Parsing Bullshit
import configparser
config = configparser.ConfigParser()
config.sections()

## EXTERNAL PYTHON FILES
import src.components.nighttabjson_to_csv as nt_to_csv
import src.components.browser_bookmarks_to_csv as bm_to_csv

## Constants will be in the config.conf file so use that please !!!
config.read('src\config.conf')

config['DEFAULT']['BmToCsv']
config['DEFAULT']['NtToCsv']

input()

## Firefox / Google Bookmarks - input file full, output folder location (will override and replace!)
# bm_to_csv.parse(f'{config['DEFAULT']['UneditedFolder']}',config['DEFAULT']['BmToCsv'])

# FIX FIX FIX FIX FIX FIX FIX!!!!!!!

## NightTab Stuff...
nt_to_csv.parse()