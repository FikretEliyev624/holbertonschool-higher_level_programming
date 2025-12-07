#!/usr/bin/python3
"""
Basic Serialization Module:
- Serialize a Python dictionary to a JSON file
- Deserialize a JSON file to a Python dictionary
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.
    
    Args:
        data (dict): Dictionary to serialize.
        filename (str): Path to the output JSON file.

    Note:
        Existing file with the same name will be overwritten.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): Path to the JSON file.

    Returns:
        dict: Deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
