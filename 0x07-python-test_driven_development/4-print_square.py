#!/usr/bin/python3

"""
Defines a function that prints a square with the character #.
"""


def print_square(size):
    """ Return a printed square of size 'size' """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise TypeError("size must be >= 0")

    # Create and print the square.
    size = int(size)
    print('\n'.join(['#' * size] * size))
