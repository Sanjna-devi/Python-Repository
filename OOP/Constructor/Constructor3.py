#Constructor with Default Values
# This example shows how a constructor can use default values
# if no arguments are provided during object creation.

class Employee:
    """
    A simple class representing an employee.
    The constructor assigns default values if no parameters are given.
    """
    def __init__(self, name="Unknown", salary=0):
        # Initialize employee attributes
        # Default values will be used if arguments are not provided
        self.name = name
        self.salary = salary

# Creating an object without passing arguments
# Default values will be used
e1 = Employee()

# Creating an object with custom values
e2 = Employee("Rahul", 30000)

# Display employee information
print(e1.name, e1.salary)
print(e2.name, e2.salary)
