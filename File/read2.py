# This program reads a file line by line
# using the readline() method.

# Step 1: Open the file in read mode
f = open(r"C:\Users\hp\OneDrive\Documents\python\File\data.txt","r")

# Step 2: Read the first line
line1 = f.readline()
print(line1)

# Step 3: Read the second line
line2 = f.readline()
print(line2)

# Step 4: Close the file
f.close()