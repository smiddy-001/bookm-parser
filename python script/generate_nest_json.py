import json

def generate(open_file, output_file, root_id=1):
    with open(open_file, 'r') as file:
        data = json.load(file)

    for item in data:
        item['children'] = []  # Add a 'children' key to each item

    # Build the tree structure by assigning children to their respective parents
    for item in data:
        parent = item.get('parent', '')
        if parent is not None:
            for parent_item in data:
                if parent_item.get('id', '') == parent:
                    parent_item['children'].append(item)
                    break

    # Find the root node with the specified root_id
    root = None
    for item in data:
        if item.get('id', '') == root_id:
            root = item
            break

    if root is None:
        print(f"Root node with ID {root_id} not found.")
        return

    # Perform DFS starting from the root node
    dfs(root)

    # Create a new list containing only the root node
    new_data = [root]

    # Overwrite the JSON file with modified data
    with open(output_file, 'w') as file:
        json.dump(new_data, file, indent=4)

def dfs(node):
    # process_node(node)
    for child in node['children']:
        dfs(child)

# def process_node(node):
    # Replace with your desired processing logic
    # print(f"Node: {node['id']}, Parent: {node['parent']}, Title: {node['title']}, URL: {node['url']}, Type: {node['type']}")
    # Additional processing logic if needed
