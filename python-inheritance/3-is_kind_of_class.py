#!/usr/bin/python3
"""
Function that checks if an object is an instance of, 
or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)
