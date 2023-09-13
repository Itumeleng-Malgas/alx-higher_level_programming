#!/usr/bin/python3
"""Defines a base class BaseGeometry."""


class BaseGeometry:
    """defines all geometry related methods"""

    def area(self):
        """raise an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the given value is an integer.

        Args:
            name  (str): Always of string type
            value (int): Integer expected, needs validation
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

