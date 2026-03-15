# This program demonstrates how a function
# can use a default parameter value.

# Step 1: Define a function named add
# 'a' is a required parameter
# 'b' is a default parameter with value 3
def add(a,b = 3):
    add=a+b
    return add

# Step 2: Call the function
# Here we only pass value for 'a'
# So Python automatically uses b = 3
result = add(2)

#print the result
print(result)