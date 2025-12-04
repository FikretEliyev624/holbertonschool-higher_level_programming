#!/usr/bin/python3
"""
Module providing function to save Python object as JSON into a file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Args:
        my_obj: JSON serializable Python object
        filename (str): File path/name to write into
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
