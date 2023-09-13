#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """writes contents to a file
    Args:
        filename (str): file name to write to
        text (str):     contents to be wriitten
    Returns: The number of chars written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
