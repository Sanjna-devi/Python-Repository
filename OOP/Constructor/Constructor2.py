#Default Constructor in Python
# If we do not define a constructor (__init__), Python automatically
# provides a default constructor that allows objects to be created.

class Car:
    """
    A simple class with no attributes or constructor.
    Python automatically creates a default constructor.
    """
    pass

# Creating an object of the Car class
c1 = Car()

# Printing the object to show that it was successfully created
print("Car object created:", c1)
