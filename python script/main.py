import sqlite_to_json_raw
import clean_json
import generate_nest_json

import spotify_data_rip

# CONSTANTS

temp_folder = "tmp"
operating_sys = ""
browser = ""
output_file_cleaned = (temp_folder+"\\bookmarks_clean.json")
output_file = (temp_folder+"\\bookmarks_raw.json")
final_output_file = ("bookmarks.json")

root_id = "3"

show_bookmarks_menu = False
show_other_bookmarks = False

user_links = {
    "spotify":"https://open.spotify.com/user/cookieplotso",
    "pinterest": "https://www.pinterest.nz/riileysmith1998/",
    "youtube": "https://www.youtube.com/@rileysmith9201/"
}

def main():
    # ---
    # Rips the info from the places.sqlite on the users local system
    # ---

    # Generates a bookmarks_raw.json
    sqlite_to_json_raw.export_bookmarks_to_json(operating_sys, browser, output_file)

    # Remove the (91) / (122) / (1) and remove the "- YouTube" from youtube titles 
    clean_json.clean_youtube_title(output_file)
    # Process titles into 'Super Titles', turns category (TITLE) into category - subcategory

    # [] and {} into ()
    clean_json.universal_parenthesis(output_file)
    
    # lints titles
    clean_json.process_titles(output_file)

    # removes dud id's such as mobile bookmarks, tabs, bookmarks menu and all that useless shaz 
    # and mushes all previous bookmarks associated to those categories to id 3 aka bookmarks toolbar
    clean_json.remove_unnecessary(output_file, output_file_cleaned, [2, 4, 5, 6])

    # ---
    # pinterest / spotify / youtube playlist mixer
    # ---

    # this process is non reversable / it obtains image data that cannot 
    # be put back into the sqlite file if you want that data back, you have
    # to concatinate some data
    spotify_data_rip.get(output_file_cleaned, user_links["spotify"])

    # generates bookmarks in foldered nest
    generate_nest_json.generate(output_file_cleaned, final_output_file)

    # 


main()