#!/usr/bin/python3
"""Write a function that appends a string to a text file (UTF8)"""


def append_write(filename="", text=""):
    """appends contents to a file
    Args:
        filename (str): file name to write to
        text (str):     contents to be appended
    Returns: The number of chars addded
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
