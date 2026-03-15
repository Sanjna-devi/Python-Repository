# Description:
# This program opens a text file, reads its
# content, prints the data, and shows the
# data type of the content

# Step 1: Open the file in read mode ("r")
f = open(r"C:\Users\hp\OneDrive\Documents\python\File\data.txt","r")

# Step 2: Read the entire file content
data = f.read()

# Step 3: Print the file content
print(data)

# Step 4: Print the type of the data
# read() always returns a string
print(type(data))

# Step 5: Close the file
f.close()