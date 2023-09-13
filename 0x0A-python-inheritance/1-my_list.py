#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Implements print_sorted function"""

    def print_sorted(self):
        """Print a list sorted ascending order."""
        print(sorted(self))
