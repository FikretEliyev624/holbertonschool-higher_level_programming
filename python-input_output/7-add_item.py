#!/usr/bin/python3
import sys
from pathlib import Path
# Import custom functions to save and load JSON files
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the JSON file exists; if yes, load its content, otherwise initialize an empty list
if Path(filename).exists():
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments (excluding the script name) to the list
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(items, filename)
