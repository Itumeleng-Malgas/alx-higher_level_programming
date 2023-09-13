#!/usr/bin/python3
"""defines a Rectangle, a BaseGeometry method"""


BaseGeometry = __import__("8-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """implements area a method of BaseGeometry super class"""

    def area(self):
        """compute the area with given width and height"""
        return self._width * self._height

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self._width, self._height)
