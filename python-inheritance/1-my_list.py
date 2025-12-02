#!/usr/bin/python3
"""
Module that defines MyList class inheriting from list.
"""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Sorting list"""
        print(sorted(self))
