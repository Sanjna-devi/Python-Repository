#Encapsulation Using Getter Method
# This demonstrates how to access a private attribute
# safely using a method (getter).

class Student:
    """
    A class representing a student.
    The marks attribute is private and accessed via a getter.
    """
    def __init__(self, marks):
        # Private attribute
        self.__marks = marks  

    def get_marks(self):
        #Getter method to access the private attribute __marks
        return self.__marks
    
# Creating an object
s = Student(85)

# Creating an object
print(s.get_marks())  
