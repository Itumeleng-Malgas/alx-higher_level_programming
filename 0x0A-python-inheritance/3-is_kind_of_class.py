#!/usr/bin/python3
"""Defines a function to check if obj is an instance of a given class"""


def is_kind_of_class(obj, a_class):
    """
    check if obj is inherited or is an instance of a_class

    Args:
        obj (any):      The given obj.
        a_class (type): The class to check against

    Returns:
        True, if obj is an instance of a_class, otherwise false.
    """

    if isinstance(obj, a_class):
        return True
    return False
