# This example demonstrates encapsulation in Python.
# A private attribute cannot be accessed directly outside the class,
# so we use a method to access it.

class Student:
    """
    A class representing a student.
    Demonstrates how private attributes can be accessed
    through a class method.
    """

    def __init__(self, name, marks):
        # Public attribute
        self.name = name
        # Private attribute (name starts with double underscore)
        self.__marks = marks

    def show_marks(self):
        # Method used to access the private attribute
        print("Marks:", self.__marks)

# Creating an object of the Student class
s1 = Student("Sanjna", 90)
# Calling the method to display marks
s1.show_marks()
