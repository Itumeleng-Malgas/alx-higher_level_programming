#!/usr/bin/python3
"""defines a Square, a BaseGeometry method"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """implements area a method of BaseGeometry super class"""

    def __init__(self, size):
        """Initializes a Square an instance with size"""
        self.integer_validator("size", size)
        self._size = size

    def area(self):
        """compute the area with given width and height"""
        return self._size * self._size
