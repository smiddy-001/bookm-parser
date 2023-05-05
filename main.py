
##

## Imports

##

import csv
from bs4 import BeautifulSoup

##

## Constants

##

input_bookmark_file = 'bookmarks.html'
output_bookmark_file = 'bookmarks'



##

## Firefox / Google Bookmarks

##


with open(input_bookmark_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all divs with article information
header_divs = soup.find_all(['h3', 'a'])

# Open a new CSV file to write the data to
with open(output_bookmark_file+'.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Title', 'Link', 'Depth'])

    # Loop through each div and extract the information
    for div in header_divs:
        # Extract the title from the h3 tag or a tag
        if div.name == 'h3':
            title = div.text.strip()
            depth = len(div.find_parents(['dl', 'ul'])) + 1
        else:
            title = div.text.strip()
            depth = len(div.find_parents(['dl', 'ul', 'ol'])) + 1

        # Extract the link and href attribute from the a tag
        if div.name == 'a':
            link = div['href']
        else:
            link = ''

        # Write the data to the CSV file
        writer.writerow([title, link, depth])


##

## NightTab Stuff...

##

