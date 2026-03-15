#class method
# Class methods are bound to the class, not the object.
# They can modify class variables and are marked with @classmethod.

class Student:
    """
    A class representing a student.
    Demonstrates the use of a class method to modify a class variable.
    """
     # Class variable shared by all instances
    school = "ABC School"  

    @classmethod
   
    def change_school(cls, new_name):
        cls.school = new_name

# Accessing the class variable
print(Student.school)

# Using class method to change the class variable
Student.change_school("XYZ School")
print(Student.school)
