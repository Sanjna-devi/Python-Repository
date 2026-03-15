#Hierarchical inheritance
# Multiple child classes can inherit from the same parent class.
# Each child gets access to the parent's methods and attributes.

class Parent:
    #Parent class with a simple method.
    def show(self):
        print("Parent class")

class Child1(Parent):
    #Child1 inherits from Parent.
    pass

class Child2(Parent):
    #Child2 inherits from Parent.
    pass

# Creating objects of both child classes
c1 = Child1()
c2 = Child2()


# Both child objects can access the method from Parent class
c1.show()
c2.show()
