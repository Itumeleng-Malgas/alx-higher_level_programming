#!/usr/bin/python3
"""The first Base class"""


class Base:
    """Base class representation"""
    _nb_objects = 0

    def __init__(self, id=None):
        """ Base class initialization """

        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    def integer_validator(self, name, value, isXY=False):
        """ checks if the given value is an int and <= 0 """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0 and not isXY:
            raise ValueError("{} must be > 0".format(name))

        if value < 0 and isXY:
            raise ValueError("{} must be >= 0".format(name))
