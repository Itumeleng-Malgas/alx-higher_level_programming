#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):

    def print_sorted(self):
        """Print a list sorted ascending order."""
        print(sorted(self))
