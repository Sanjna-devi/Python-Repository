# In Python, when an operation involves two different numeric types,
# the "lower" type is automatically converted to the "higher" type.
# Here, integer 'a' is converted to float to match 'b'.
# This ensures the operation (addition) is safe and precise.
a=2
b=4.25
sum=a+b
print(sum)