# Attributes with double underscores (__) are treated as private.
# They cannot be accessed directly outside the class.

class Student:
    """
    A class representing a student.
    Demonstrates how private attributes work in Python.
    """
    def __init__(self, name, marks):
        # Public attribute
        self.name = name
        # Private attribute (cannot be accessed directly outside the class)
        self.__marks = marks   # private attribute

# Creating an object
s1 = Student("Sanjna", 90)

# Accessing public attribute (works normally)
print(s1.name)       

# Attempting to access private attribute directly
# This will raise an AttributeError
print(s1.__marks)    
