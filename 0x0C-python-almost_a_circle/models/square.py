#!/usr/bin/python3
"""module that defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """super initializing attributes"""
        super().__init__(
            size, size, x, y, id
        )

    def __str__(self):
        """returns str representation of the class"""
        st = "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width
        )
        return st

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns class attributes to argument
            Args:
                args: non key-word argument
                kwargs: keyword argument"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            for key in kwargs.keys():
                if key == "id":
                    self.id = kwargs["id"]
                if key == "size":
                    self.size = kwargs["size"]
                if key == "x":
                    self.x = kwargs["x"]
                if key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """return dictionary representation of the attributes"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
