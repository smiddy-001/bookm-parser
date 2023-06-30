import sqlite_to_json_raw
import clean_json
import generate_nest_json

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


def main():

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

    # generates bookmarks in foldered nest
    generate_nest_json.generate(output_file_cleaned, final_output_file)

main()