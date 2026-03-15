# This example demonstrates that each object has its own copy
# of instance attributes. Changing one object does not affect others.

class Student:
    """
    A class representing a student.
    Each object stores its own name and age.
    """
    def __init__(self, name, age):
        # Instance attributes (unique for each object)
        self.name = name
        self.age = age

# Creating two objects of the Student class
s1 = Student("Ali", 20)
s2 = Student("Sara", 22)

# Accessing instance attributes of s1
print(s1.name)  
print(s1.age)   

# Accessing instance attributes of s2
print(s2.name)  
print(s2.age)   

# Changing the age of the first object
s1.age = 21

# Showing that only s1 changed
print(s1.age)   
print(s2.age)   
