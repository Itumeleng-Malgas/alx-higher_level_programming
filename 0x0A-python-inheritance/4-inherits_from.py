#!/usr/bin/python3
"""checks if a given object is only sub class of a specified class"""


def inherits_from(obj, a_class):
    """
    check if obj is a sub class of a_class

    Args:
        obj (any):      The given object
        a_class (type): The class to check against

    Returns: True, if obj is inherited from a_class, otherwise false
    """

    if issubclass(type(obj), a_class):
        return True
    return False
