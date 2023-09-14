#!/usr/bin/python3
"""define a class student"""


class Student:
    """Student class representation"""

    def __init__(self, first_name, last_name, age):
        """ Student class initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dict representation of a student obj"""
        if type(attrs) == list and all(type(e) == str for e in attrs):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for x, y in json.items():
            setattr(self, x, y)
