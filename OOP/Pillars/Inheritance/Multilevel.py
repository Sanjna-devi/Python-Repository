#Multilevel Inheritance
# A class can inherit from another class, forming a chain of inheritance.
# The child class can access methods from all ancestor classes.

class Grandparent:
    #Top-level parent class.
    def house(self):
        print("House")

class Parent(Grandparent):
    #Inherits from Grandparent.
    pass

class Child(Parent):
    #Inherits from Parent, forming multilevel inheritance.
    pass

# Creating an object of the Child class
# The object can access methods from Parent and Grandparent
c = Child()

# Calling a method from the top-most ancestor (Grandparent)
c.house()
