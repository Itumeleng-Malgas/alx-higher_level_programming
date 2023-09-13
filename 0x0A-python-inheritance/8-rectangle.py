#!/usr/bin/python3
"""defines a Rectangle, a BaseGeometry method"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """initializes Rectangle an instance of BaseGeometry sub class"""

    def __init__(self, width, height):
        """ initializes the Rectangle object """
        self.integer_validator("width", width)
        self._width = width

        self.integer_validator("height", height)
        self._height = height
