#!/usr/bin/python3

"""A module thats used to add two integers"""


def add_integer(a, b=98):
    """A function that adds two integers

    Args:
        a (int/ float): integer to be added
        b (int/ float): integer to be added with default value 98
        """

    if a is None or (type(a) is not int and type(a) is not float):
        """a must be an int or float else raise TypeError"""
        raise TypeError("a must be an integer")
    if b is None or (type(b) is not int and type(b) is not float):
        """b must be an int or float else raise TypeError"""
        raise TypeError("b must be an integer")
    return int(a) + int(b)
