#!/usr/bin/python3
"""Class Square definition."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize class Square.

        Args:
            size (int): Size of the square.
        """
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
