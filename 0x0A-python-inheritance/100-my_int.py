#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """class that twist comparision"""
    def __eq__(self, value):
        """changes the equal to not equal"""
        return self.real != value

    def __ne__(self, value):
        """changes not equal to equal"""
        return self.real == value
