#!/usr/bin/python3

"""defines a class student"""


class Student:
    """Class description of a student"""

    def __init__(self, first_name, last_name, age):
        """Initializing student attribute

        Args:
            first_name(str): first name of the student
            last_name(str): last name of the student
            age(int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of the class"""
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
