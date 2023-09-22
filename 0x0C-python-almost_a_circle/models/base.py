#!/usr/bin/python3
"""The first Base class"""
import json, csv, turtle


class Base:
    """Base class representation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base class initialization """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value, isXY=False):
        """ checks if the given value is an int and <= 0 """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0 and not isXY:
            raise ValueError("{} must be > 0".format(name))

        if value < 0 and isXY:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
