#!/usr/bin/python3
"""json module"""
import json


def from_json_string(my_str):
    """converts a json string to python"""
    return json.loads(my_str)
