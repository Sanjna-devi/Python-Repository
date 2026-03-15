#Using super() to Call Parent Constructor in Python
# When a child class overrides the constructor (__init__),
# we can use super() to call the parent class constructor
# and initialize parent attributes.

class Person:
   #Parent class representing a person.

    def __init__(self, name):
        self.name = name

class Student(Person):
    #Child class representing a student.
    def __init__(self, name, marks):
        # Call parent constructor to initialize 'name'
        super().__init__(name)   
         # Initialize child-specific attribute
        self.marks = marks

# Creating a Student object
s1 = Student("Sanjna", 90)

# Accessing attributes inherited from parent and defined in child
print(s1.name)
print(s1.marks)
