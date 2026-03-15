# Static methods belong to the class rather than an instance.
# They do not access instance attributes or methods,
# and can be called directly using the class name.

class Math:
    """
    A class demonstrating static methods.
    Static methods perform operations without needing an object.
    """
    @staticmethod
    def add(a, b):
        #Returns the sum of two numbers.
        return a + b

    @staticmethod
    def multiply(a, b):
        #Returns the product of two numbers.
        return a * b

# Calling static methods using the class name (no object needed)
print(Math.add(5, 3))        
print(Math.multiply(4, 6))  
