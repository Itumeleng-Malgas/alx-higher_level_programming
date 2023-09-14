#!/usr/bin/python3
"""defines a class Student"""


class Student:
    """represent a student obj"""

    def __init__(self, first_name, last_name, age):
        """initialize a student obj"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
