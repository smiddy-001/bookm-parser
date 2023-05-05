import json
import pandas as pd

# Constants
input_file = 'nightTab.json'
output_file = 'nt_csv.csv'

# Load JSON object
with open(input_file, 'r') as f:
    data = json.load(f)

# Extract the bookmark items
bookmark_items = []
for i in range(len(data['bookmark'])):
    items = data['bookmark'][i]['items']
    bookmark_items.extend(items)

# Extract the 'Title' and 'Link' information for each item
titles = [item['display']['name']['text'] for item in bookmark_items]
links = [item['url'] for item in bookmark_items]

# Create the DataFrame with 'Title', 'Link', and 'Depth' columns
df = pd.DataFrame({'Title': titles, 'Link': links, 'Depth': 1})

# Save the DataFrame to a CSV file
df.to_csv(output_file, index=False)
