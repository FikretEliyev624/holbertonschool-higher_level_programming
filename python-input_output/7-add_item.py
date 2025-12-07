#!/usr/bin/python3
"""
Add all command-line arguments to a list and save them to a JSON file.
If the file exists and is non-empty, the existing list is loaded first.
"""

import sys
from pathlib import Path

# Import custom functions to save and load JSON files
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

# Load existing list if file exists and is not empty
file_path = Path(filename)
if file_path.exists() and file_path.stat().st_size > 0:
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments (excluding the script name) to the list
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(items, filename)
