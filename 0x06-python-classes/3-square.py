#!/usr/bin/python3

"""class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """ Initializing a new square.

        Args:
            size(int): size of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
