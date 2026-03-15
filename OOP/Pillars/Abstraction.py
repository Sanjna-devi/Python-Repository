#Abstract Class in Python
# Abstract classes define methods that must be implemented
# by subclasses. They cannot be instantiated directly.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Abstract base class representing a vehicle.
    Subclasses must implement the start() method.
    """

    @abstractmethod
    def start(self):
        #Abstract method to start the vehicle
        pass

class Car(Vehicle):
    """
    Subclass of Vehicle that provides implementation
    for the abstract method start().
    """
    def start(self):
        print("Car started!")

# Creating an object of Car and calling start()
c = Car()
c.start()  
