#!/usr/bin/python3

"""Module that prints a full name"""


def say_my_name(first_name, last_name=""):
    """Function that prints out a full name with first name and last name,
        with the string e.g``My name is Michael Forster``.
        Michael as first name and Forster as last name

        Args:
            first_name(string): first name of user must be string else raise TypeError
            last_name(string): last name of user must be string else raise TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
