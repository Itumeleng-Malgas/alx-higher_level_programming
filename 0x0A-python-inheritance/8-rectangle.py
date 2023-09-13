#!/usr/bin/python3
"""defines a Rectangle, a BaseGeometry method"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        integer_validator("width", width)
        self.width = width

        integer_validator("height", height)
        self.height = height
