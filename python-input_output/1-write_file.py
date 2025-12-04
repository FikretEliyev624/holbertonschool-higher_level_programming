#!/usr/bin/python3
"""
Docstring for 1-write_file
"""


def write_file(filename="", text=""):
    """
    Docstring for write_file
    :param filename: Description
    :param text: Description
    """
    with open(filename, "x") as f:
        f.write(text)
        return len(text)
