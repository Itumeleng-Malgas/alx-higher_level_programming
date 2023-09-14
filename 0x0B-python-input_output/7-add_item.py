#!/usr/bin/python3
"""
defines a script that adds all arguments to a Python list,
and then save them to a file
"""
import sys


def load_add_save():
    save_to_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_file = __import__("6-load_from_json_file").load_from_json_file

    try:
        items = load_from_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_file(items, "add_item.json")

if __name__ == "__main__":
    load_add_save()
