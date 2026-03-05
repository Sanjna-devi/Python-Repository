# In Python, we can explicitly convert a value from one type to another.
# Here, the float 4.25 is explicitly converted to an integer using int().
# After conversion, arithmetic operations proceed with the new type.
# Note: int() truncates the decimal part (does NOT round).
a=2
b=int(4.25)
sum=a+b
print(sum)