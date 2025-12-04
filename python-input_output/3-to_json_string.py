#!/usr/bin/python3
import json

"""
Module that converts a Python object to its JSON representation.
"""


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.

    Args:
        my_obj: Any serializable Python object (list, dict, str, int, etc.)

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
