import sqlite3
import json
import os


def export_bookmarks_to_json(operating_system, browser, output_file='bookmarks_raw.json'):
    # Find the Firefox profile directory
    firefox_profile_dir = ""
    mozilla_appdata = os.getenv("APPDATA")

    if mozilla_appdata:
        profiles_dir = os.path.join(mozilla_appdata, "Mozilla", "Firefox", "Profiles")
        profile_dirs = [d for d in os.listdir(profiles_dir) if os.path.isdir(os.path.join(profiles_dir, d))]

        for profile_dir in profile_dirs:
            if os.path.isfile(os.path.join(profiles_dir, profile_dir, "places.sqlite")):
                firefox_profile_dir = os.path.join(profiles_dir, profile_dir)
                break

    if not firefox_profile_dir:
        print("Firefox profile directory not found.")
        exit()

    # Connect to the Firefox bookmarks database
    conn = sqlite3.connect(os.path.join(firefox_profile_dir, "places.sqlite"))
    conn.row_factory = sqlite3.Row  # Return results as dictionaries
    cursor = conn.cursor()

    # Execute a query to fetch bookmark data including folders and bookmarks
    cursor.execute("""
        SELECT
            b.id, b.parent, b.title, p.url, b.type
        FROM
            moz_bookmarks b
            LEFT JOIN moz_places p ON b.fk = p.id
        WHERE
            b.type IN (1, 2, 2) OR (b.type = 0 AND b.title != '')
    """)

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Define a list to store the bookmarks and folders
    bookmarks = []

    # Iterate over the rows and extract relevant data
    for row in rows:
        item = {
            "id": row["id"],
            "parent": row["parent"],
            "title": row["title"],
            "url": row["url"] if row["type"] != 2 else None,  # Set URL to None for folders
            "type": row["type"]
        }
        bookmarks.append(item)

    # Close the database connection
    conn.close()

    # Write the bookmarks as a JSON array to the file
    with open(output_file, "w") as f:
        json.dump(bookmarks, f)

    print("Bookmarks exported successfully to", output_file)
