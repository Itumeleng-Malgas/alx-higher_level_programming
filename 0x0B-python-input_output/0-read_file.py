#!/usr/bin/python3
"""defines a  function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """reads file contents and then prints it stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        print(file_contents, end="")
