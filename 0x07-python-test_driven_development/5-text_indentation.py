#!/usr/bin/python3

"""
Defines a function that prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """Prints 2 new lines after each occurrence: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace '.', '?', and ':' with '\n\n' and split into lines
    lines = "".join([c if c not in ('.', '?', ':') else
                     c + '\n\n' for c in text]).split('\n\n')

    # Print each line after stripping leading whitespace
    for line in lines:
        print(f"\n{line.lstrip()}")
