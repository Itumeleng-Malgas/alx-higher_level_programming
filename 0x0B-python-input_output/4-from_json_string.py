#!/usr/bin/python3
"""defines a from_json_string function"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.load(my_str)
