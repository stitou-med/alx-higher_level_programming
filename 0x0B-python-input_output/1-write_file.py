#!/usr/bin/python3
"""defines a write file function"""


def write_file(filename="", text=""):
    """function that writes to a file

    Args:
        filename: name of file to write to,
            if none new one is created
        text: the text to write"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
