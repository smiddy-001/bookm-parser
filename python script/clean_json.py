import json
import re

prepositions = [
    'about', 'above', 'across', 'after', 'against', 'along', 'among', 'around', 'as',
    'at', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond', 'by',
    'concerning', 'considering', 'despite', 'down', 'during', 'except', 'for', 'from',
    'in', 'inside', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'out',
    'outside', 'over', 'past', 'regarding', 'round', 'since', 'through', 'throughout', 'to',
    'toward', 'under', 'underneath', 'until', 'up', 'upon', 'with', 'within', 'without'
]


def clean_youtube_title(open_file):
    with open(open_file) as file:
        data = json.load(file)

    modified_data = []  # Create a new list to store modified items

    # Iterate over the items in the JSON data
    for item in data:
        url = item.get('url', '')
        title = item.get('title', '')
        # item_type = item.get('type', '')

        # if item_type == 2:
        #     # Folders should be included without modification
        #     modified_data.append(item)
        if url and title:
            if url.startswith('https://www.youtube'):
                modified_title = title

                # Check if the title ends with ' - YouTube'
                if modified_title.endswith(' - YouTube'):
                    # Remove the ending ' - YouTube'
                    modified_title = modified_title[:-10].strip()

                # Remove (number) prefix
                modified_title = re.sub(
                    r'\(\d+\)\s*', '', modified_title).strip()

                item['title'] = modified_title
                # Add the modified item to the new list

        modified_data.append(item)

    # Write the modified data back to the JSON file
    with open(open_file, 'w') as file:
        json.dump(modified_data, file, indent=4)

    print("Modified data saved successfully.")


def universal_parenthesis(open_file, left_brace='(', right_brace=')'):
    with open(open_file, 'r') as file:
        data = json.load(file)

    for item in data:
        title = item.get('title')
        if title:
            # Capitalize the first letter of the title
            title = title.title()

            # Replace characters with dashes
            title = title.replace(']', right_brace)
            title = title.replace('}', right_brace)
            title = title.replace(')', right_brace)
            title = title.replace('>', right_brace)
            title = title.replace('<', left_brace)
            title = title.replace('[', left_brace)
            title = title.replace('{', left_brace)
            title = title.replace('(', left_brace)
            title = re.sub(
                r'(?<=[\(\[{\}>\]])\s*|\s*(?=[\)\]}>])', ' ', title.strip())

            item['title'] = title

    # Overwrite the JSON file with modified data
    with open(open_file, 'w') as file:
        json.dump(data, file, indent=4)

    print('JSON file has been modified and saved.')


def process_titles(open_file, dash_replacer='•'):
    with open(open_file, 'r') as file:
        data = json.load(file)

    for item in data:
        title = item.get('title')
        if title:
            # print(f'\n---\nold - {title}')
            title += ' '
            # Capitalize the first letter of the title
            title = title.lower()

            # Replace characters with dashes
            title = title.replace('•', '-')
            title = title.replace('|', '-')
            title = title.replace('+', '-')
            title = title.replace('#', '-')
            title = title.replace('%', '-')
            title = title.replace('^', '-')
            title = title.replace('\\', '-')
            title = title.replace('*', '-')
            title = title.replace('~', '-')
            title = title.replace('/', '-')
            title = title.replace('@', ' at ')
            title = title.replace('&', ' and ')
            title = title.replace('+', '-')
            title = title.replace(':', ' - ')

            # Remove quotes
            title = title.replace('\"', '')
            title = title.replace('\'', '')

            # Perform other replacements
            title = title.replace(' ep ', ' ')
            title = title.replace(' lp ', ' ')
            title = title.replace(' single ', ' ')
            title = title.replace(' open-source ', ' open source ')
            title = title.replace(' , full show, sound ', ' ')
            title = title.replace(' official audio ', ' ')
            # Removes the substring 'Lyric Video' from the title.
            title = title.replace(' lyric video ', ' ')
            # Removes the substring 'Lyrics' from the title.
            title = title.replace(' lyrics ', ' ')
            # Removes the substring 'HQ' from the title.
            title = title.replace(' hq ', ' ')
            # Removes the substring 'HD' from the title.
            title = title.replace(' hd ', ' ')
            # Removes the substring 'Remix' from the title.
            title = title.replace(' remix ', ' ')
            # Removes the substring 'Feat.' from the title.
            title = title.replace(' feat ', ' ')
            # Removes the substring 'Feat.' from the title.
            title = title.replace(' feat. ', ' ')
            # Removes the substring 'ft.' from the title.
            title = title.replace(' ft ', ' ')
            # Removes the substring 'ft.' from the title.
            title = title.replace(' ft. ', ' ')
            title = title.replace(' official music video ', ' ')
            title = title.replace(' music video ', ' ')
            title = title.replace(' official video ', ' ')
            title = title.replace(' videoclip official ', ' ')
            title = title.replace(' npr music tiny desk concert ', ' ')
            title = title.replace(' 4k ', ' ')
            title = title.replace(' 2k ', ' ')
            title = title.replace(' 1080 ', ' ')
            title = title.replace(' 1440 ', ' ')
            title = title.replace(' 2560 ', ' ')
            title = title.replace(' 2560 ', ' ')
            title = title.replace(' p ', ' ')
            title = title.replace(' px ', ' ')
            title = title.replace(' pt', ' ')
            title = title.replace(' pt.', ' ')

            # Remove parentheses and their contents
            title = re.sub(r'\s*\([^)]*\)', '', title)

            # Apply spacing around brackets and hyphens
            title = re.sub(
                r'(?<=[\(\[\{<])\s*-|\s*-(?=[\)\]\}>])', ' - ', title.strip())
            title = re.sub(
                r'(?<=[\(\[\{<])\s*|\s*(?=[\)\]\}>])', ' ', title.strip())

            # Capture only the first two blocks of text separated by hyphens
            if len(re.sub(r'^([^-\n]*-[^-\n]*).*$', r'\1', title)) <= 32:
                title = re.sub(r'^([^-\n]*-[^-\n]*).*$', r'\1', title)
            else:
                title = re.sub(r'^([^-\n]*).*$', r'\1', title)

            # Add a space around the hyphen
            title = re.sub(r'(?<=\S)-(?=\S)', r' - ', title)

            # Replace consecutive hyphens with a single hyphen
            title = re.sub(r'-{2,}', '-', title)

            # Remove non-alphabetical characters at the end of the title
            title = re.sub(r'[^a-zA-Z]+$', '', title)

            # Remove double, triple, or multiple consecutive spaces
            title = re.sub(r'\s{2,}', ' ', title)

            # Check if the title ends with a preposition and remove it
            last_word = title.split()[-1].lower()
            if last_word in prepositions:
                title = ' '.join(title.split()[:-1])

            # replaces dashes with specified replacer
            title = title.replace('-', dash_replacer)

            # print(f'new - {title}')
            item['title'] = title

    # Overwrite the JSON file with modified data
    with open(open_file, 'w') as file:
        json.dump(data, file, indent=4)

    print('JSON file has been modified and saved.')

    # {
    #     "id": 1,
    #     "parent": 0,
    #     "title": "",
    #     "url": null,
    #     "type": 2
    # },
    # {
    #     "id": 2,
    #     "parent": 1,
    #     "title": "menu",
    #     "url": null,
    #     "type": 2
    # },
    # {
    #     "id": 3,
    #     "parent": 1,
    #     "title": "toolbar",
    #     "url": null,
    #     "type": 2
    # },
    # {
    #     "id": 4,
    #     "parent": 1,
    #     "title": "tags",
    #     "url": null,
    #     "type": 2
    # },
    # {
    #     "id": 5,
    #     "parent": 1,
    #     "title": "unfiled",
    #     "url": null,
    #     "type": 2
    # },
    # {
    #     "id": 6,
    #     "parent": 1,
    #     "title": "mobile",
    #     "url": null,
    #     "type": 2
    # },

def remove_unnecessary(open_file, output_file, remove_id_list=[2, 4, 5, 6]):
    with open(open_file, 'r') as file:
        data = json.load(file)
    
    # Remove items with specified IDs
    data = [item for item in data if item['id'] not in remove_id_list]


    # Convert the modified JSON object back to a JSON string
    updated_json = json.dumps(data, indent=4)

    # Overwrite the JSON file with modified data
    with open(output_file, 'w') as file:
        file.write(updated_json)