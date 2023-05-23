

# This is a script designed to pull rip and reorganise and reformat html,
# json and other wierd configs of bookmarks, turn them into csv format and 
# use that csv in a local hoseted webpage and use that webpage as a quicklink 
# bookmarks new tab.

## Imports
import yaml
import python.components.nighttabjson_to_csv as nt_to_csv
import python.components.browser_bookmarks_to_csv as bm_to_csv

## Constants will be in the config.yml file so use that please !!!
with open('./python/config.yml', 'r') as f:
    config = yaml.safe_load(f)

bookmark_py = config['Imports']['BmToCsv']
nighttab_py = config['Imports']['NtToCsv']
originals_location = config['Imports']['UneditedFolder']
seperated_location = config['Imports']['EditedFolder']

name_convention_bookmarks = config['Unedited']['BookmarkFile']
name_convention_nighttab = config['Unedited']['NightTabFile']

output_name = config['Edited']['output']

print(f'{bookmark_py}\n{nighttab_py}\n{originals_location}\n{seperated_location}\n{name_convention_bookmarks}\n{name_convention_nighttab}\n{output_name}')
# input()

## Firefox / Google Bookmarks - input file full, output folder location (will override and replace!)
# bm_to_csv.parse(f'{config['DEFAULT']['UneditedFolder']}',config['DEFAULT']['BmToCsv'])

# FIX FIX FIX FIX FIX FIX FIX!!!!!!!

print(f'.\\{originals_location}\\{name_convention_bookmarks}')
print(f'.\\{seperated_location}\\{output_name}')
## NightTab Stuff...
bm_to_csv.parse(f'{originals_location}\\{name_convention_bookmarks}',f'{seperated_location}\\{name_convention_bookmarks}-{output_name}')
nt_to_csv.parse(f'{originals_location}\\{name_convention_nighttab}',f'{seperated_location}\\{name_convention_nighttab}-{output_name}')

print('complete!')