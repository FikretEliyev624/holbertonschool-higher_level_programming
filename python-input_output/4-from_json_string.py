#!/usr/bin/python3
"""
Module converting a JSON string into its corresponding Python data structure.
"""

import json


def from_json_string(my_str):
    """
    Return Python object from JSON string.

    Args:
        my_str (str): JSON formatted string

    Returns:
        object: Python data structure (list, dict, int, str, etc.)
    """
    return json.loads(my_str)
