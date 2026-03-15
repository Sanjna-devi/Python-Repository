# This program opens a text file, writes
# data to it, and then reads the content.

# Step 1: Open the file
# "a+" mode means:
# a  -> append (add text at the end of file)
#  +  -> allows reading and writing
f =open(r"C:\Users\hp\OneDrive\Documents\python\File\data.txt","a+")

# Step 2: Write text into the file
f.write("and will be graduated  in 2029")

# Step 3: Move the cursor to the beginning of the file
# Because after writing, the cursor stays at the end
f.seek(0)

# Step 4: Read and display file content
print(f.read())

# Step 5: Close the file
f.close()