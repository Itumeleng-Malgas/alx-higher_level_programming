#!/usr/bin/python3
"""The first Base class"""
import json
import csv
import turtle


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
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves list object to JSON file """
        filename = cls.__name__ + ".json"

        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  returns an instance with all attributes already set """
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)

            dummy.update(**dictionary)

            return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, "r") as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**dicts) for dicts in list_dictionaries]

        except IOError:
            return []
