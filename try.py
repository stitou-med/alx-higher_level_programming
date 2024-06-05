import os

"""Personal try of class method
    Helped me in doing my Alx task
        lit
            """
class Human:
    
    def __init__(self, name="", age=0, complesion=""):
        self.name = name
        self.age = age
        self.complesion = complesion
        
    @property
    def name(self):
        print("Getting the name")
        
        return self.__name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            print("name cant be empty or a number")
        self.__name = value
            
    @property
    def age(self):
        print("Getting the age")
        
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print("age cant be empty or a string")
        self.__age = value
            
    @property
    def complesion(self):
        print("Getting the complesion")
        
        return self.__complesion

    @complesion.setter
    def complesion(self, value):
        if not isinstance(value, str):
            print("name cant be empty or a number")
        self.__complesion = value
            
            
    def getTheHuman(self):
        me = print("my name is {}, i am {} years old, and i am {} in complesion".format(self.__name, self.__age, self.__complesion))
        
        return me
    
def main():
    anonymous = Human()
    
    name = input("What is your name: ")
    age = int(input("What is your age: "))
    complesion = input("What is your complesion: ")
    
    anonymous.name = name
    anonymous.age = age
    anonymous.complesion = complesion
    
    print("Name: ", anonymous.name)
    print("age: ", anonymous.age)
    print("complesion: ", anonymous.complesion)
    
    print(anonymous.getTheHuman())
    
main()


"""Checking the awesome os module"""
path = "/"
dir_list = os.listdir(path)
print("files and directory in '", path, "' :")
print(dir_list)


print("Os name is: ", os.name)


size = os.path.getsize("/")
print("Size of the file is", size," bytes.")