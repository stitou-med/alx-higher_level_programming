# 0x0A-python-inheritance


## Tasks

| File | Function/ Class | Duty |
| ---- | --------------- | ---- |
| [0-lookup.py](0-lookup.py) | def lookup(obj): | returns a list of attributes and methods of a class |
| [1-my_list.py](1-my_list.py) | class MyList(list), def print_sorted() | class that prints a sorted list. Test file at [1-my_list.txt](1-my_list.txt) |
| [2-is_same_class.py](2-is_same_class.py) | def is_same_class(obj, a_class): | A fuction that checks if an object is an instance of a class |
| [3-is_kind_of_class.py](3-is_kind_of_class.py) | def is_kind_of_class(obj, a_class) | checks if an object is an instance of a class or inherited class |
| [4-inherits_from.py](4-inherits_from.py) | def inherits_from(obj, a_class) | checks if an object is an instance of an inherited class |
| [5-base_geometry.py](5-base_geometry.py) | class BaseGeometry | An empty class that does nothing |
| [6-base_geometry.py](6-base_geometry.py) | class BaseGeometry | A class that raises an exception |
| [7-base_geometry.py](7-base_geometry.py) | class BaseGeometry, def integer_validator(self, name, value) | validates value int and greater than 0. test file at [7-base_geometry.txt](7-base_geometry.txt) |
| [8-rectangle.py](8-rectangle.py) | class Rectangle(BaseGeometry) | child class of the BaseGeometry class that validates the width and height of a rectangle |
| [9-rectangle.py](9-rectangle.py) | class Rectangle(BaseGeometry), def area(self), def \_\_str\_\_(self) | implements the str method and solve the area of the rectangle from [8-rectangle.py](8-rectangle.py) |
| [10-square.py](10-square.py) | class Square, def area() | calculates the area of a square from [9-rectangle.py](9-rectangle.py) |
| [11-square.py](11-square.py) | class Square, def \_\_str\_\_() | implements str on Square code from [10-square.py](10-square.py) |
| [100-my_int.py](100-my_int.py) | class MyInt(int), def \_\_eq\_\_(value), def \_\_ne\_\_(value) | switches the duty of equal and not equal |
| [101-add_attribute.py](101-add_attribute.py) | def add_attribute(obj, attr, value) | adds attribute to an object |

# END