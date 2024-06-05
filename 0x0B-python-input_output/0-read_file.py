#!/usr/bin/python3
"""Defines a text file readng function"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as rf:
        read_file = rf.read()
        print(read_file, end="")
