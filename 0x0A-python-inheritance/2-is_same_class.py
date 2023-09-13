#!/usr/bin/python3
""" Defines a function to check if obj is instance of a given class """


def is_same_class(obj, a_class):
    """
    checks if obj is an instance of a_class

    Args:
        obj (any):      The given obj
        a_class (type): The class to check against the obj
    Returns:
        True, if obj is of type a_class, otherwise false
    """

    if isinstance(obj, a_class):
        return True
    return False
