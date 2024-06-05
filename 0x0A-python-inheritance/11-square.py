#!/usr/bin/python3
"""inherits a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size):
        """initializes the square class

        Args:
            size(int > 0): size of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        st = f"[{str(self.__class__.__name__)}] {str(self.__size)}"
        st += f"/{str(self.__size)}"
        return st
