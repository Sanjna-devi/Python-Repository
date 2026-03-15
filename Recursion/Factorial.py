# This program calculates the factorial of
# a number using recursion.

def factorial(n):

     # Base case: stopping condition
    if n == 1:      # Base case
        return 1
    
    # Recursive case: function calls itself
    return n * factorial(n - 1)

# Calling the function
print(factorial(5))
