# This example demonstrates the difference between attributes
# shared by all objects (class attributes) and attributes
# unique to each object (instance attributes).


class Student:
    # Class attribute: shared by all instances of the class
    school = "ABC School"   
   
    def __init__(self, name):
    # Instance attribute: unique for each object
        self.name = name    

s1 = Student("Ali")
s2 = Student("Sara")

print(s1.school)
print(s2.school)
