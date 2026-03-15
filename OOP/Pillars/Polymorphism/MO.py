# Method overriding
# Method overriding occurs when a child class provides
# its own implementation of a method already defined in the parent class.

class Animal:
    #Parent class with a generic sound method.
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    #Child class overriding the sound method.
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    #Child class overriding the sound method.
    def sound(self):
        print("Cat meows")

# Creating objects of child classes
d = Dog()
c = Cat()

# Calling the overridden methods
d.sound()
c.sound()
