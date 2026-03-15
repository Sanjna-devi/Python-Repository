# This program opens a file in w+ mode, writes
# content to it, then reads and prints it.


# Step 1: Open the file in "w+" mode
# "w+" -> Write and Read
#       -> Creates a new file or overwrites existing content
f=open(r"C:\Users\hp\OneDrive\Documents\p\File\new.txt","w+")

# Step 2: Write some content to the file
f.write("at mehran university of engineering and technology")

# Step 3: Move the cursor to the start of the file
# After writing, the cursor is at the end
# We must move it back to the beginning to read
f.seek(0)

# Step 4: Read the file content
print(f.read())

# Step 5: Close the file
f.close()