#Constructor with Parameters
# This example shows how to initialize object attributes
# using a constructor (__init__) with parameters.

class Student:
    """
    A simple class representing a student.
    The constructor initializes the student's name and age
    when an object is created.
    """

    def __init__(self, name, age):
        # Assign values passed during object creation
        # to instance variables
        self.name = name
        self.age = age

# Creating an object of the Student class
s1 = Student("Sanjna", 20)

# Accessing and printing the object's attributes
print(s1.name)
print(s1.age)
