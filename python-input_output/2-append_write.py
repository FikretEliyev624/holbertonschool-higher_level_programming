#!/usr/bin/python3
"""
Docstring for 2-append_write
"""


def append_write(filename="", text=""):
    """
    Docstring for append_write

    :param filename: Description
    :param text: Description
    """
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
