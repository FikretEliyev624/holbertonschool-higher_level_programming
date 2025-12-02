#!/usr/bin/python3
"""
Inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)
