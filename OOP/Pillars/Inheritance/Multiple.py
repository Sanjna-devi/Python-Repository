#Multiple inheritasnce
# A class can inherit from more than one parent class.
# The child class gains access to all methods of its parents.

class Father:
    #Parent class 1 with a skill.
    def skill1(self):
        print("Driving")

class Mother:
    #Parent class 2 with a skill.
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    #Child class inheriting from both Father and Mother.
    pass

# Creating an object of the Child class
c = Child()

# Child can access methods from both parent classes
c.skill1()
c.skill2()
