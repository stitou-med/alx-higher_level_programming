#!/usr/bin/python3
"""inherits a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits BaseGeometry class"""

    def __init__(self, width, height):
        """uses the super class function to validate width and height

        Args:
            width(int): must be int greater than 0 else error
            height(int): must be int greater than 0 else error
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """function that returns the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """str method that returns the class and width div height"""
        st = f"[{str(self.__class__.__name__)}] {str(self.__width)}"
        st += f"/{str(self.__height)}"
        return st
