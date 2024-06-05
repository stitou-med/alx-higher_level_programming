#!/usr/bin/python3
"""module that adds attribute"""


def add_attribute(obj, attr, value):
    """adds attributes to an object

    Args:
        obj: object to add the attribute
        attr: attribute to be added
        value: value of the attribute

        raises a typeerror if attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
