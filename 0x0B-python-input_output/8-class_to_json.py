#!/usr/bin/python3
"""defines class to json"""


def class_to_json(obj):
    """returnsthe dictionary description with simple data structure"""
    return obj.__dict__
