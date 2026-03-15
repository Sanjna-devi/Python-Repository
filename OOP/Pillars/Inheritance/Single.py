# Single inheritance
# Single inheritance allows a class (child) to inherit
# methods and attributes from another class (parent).

class Parent:
    #Parent class with a simple method.
    def show(self):
        print("Parent class")

class Child(Parent):
    #Child class inheriting from Parent class.
        pass

# Creating an object of the Child class.
c = Child()

# Child class can access methods of the Parent class.
c.show()
