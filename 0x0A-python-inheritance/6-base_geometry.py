#!/usr/bin/python3
"""Defines a base class BaseGeometry."""


class BaseGeometry:
    """defines all geometry related methods"""

    def area(self):
        """raise an exception when called"""
        raise Exception("area() is not implemented")
