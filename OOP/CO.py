# This example demonstrates how to create a simple class in Python
# and access its attributes using an object.

class Car:
    """
    A basic class representing a car.
    It stores simple information about a car such as
    its name, color, and brand.
    """

    # Class attributes (shared by all objects of this class)
    name = "Swift"
    color = "black"
    brand = "Toyota"

# Create an object (instance) of the Car class
car1 = Car()

# Access and display the attributes of the object
print(car1.name)
print(car1.color)
print(car1.brand)
