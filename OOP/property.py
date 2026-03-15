#Using @property Decorator in Python
# The @property decorator allows us to access a method
# like an attribute. This is often used for controlled access
# to “protected” or private variables.

class Student:
    """
    A class representing a student.
    Demonstrates the use of @property to access a variable.
    """
     
    def __init__(self, marks):
         # "Protected-like" variable (conventionally prefixed with _)
        self._marks = marks   



    @property
    def marks(self):
        return self._marks


# Creating a Student object
s1 = Student(90)

# Accessing marks like an attribute (no parentheses needed
print(s1.marks)   
