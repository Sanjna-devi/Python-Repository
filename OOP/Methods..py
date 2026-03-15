# This example demonstrates how instance methods can use
# instance attributes of an object.

class Student:
    """
    A class representing a student.
    Demonstrates the use of an instance method to access
    instance attributes.
    """

    def __init__(self, name, age):
        # Instance attributes (unique to each object)
        self.name = name    
        self.age = age      

    def greet(self):      
        """
        Instance method that uses the object's attributes
        to print a greeting message.
        """  

        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Student class
s1 = Student("Ali", 20)
# Calling the instance method
s1.greet()  
