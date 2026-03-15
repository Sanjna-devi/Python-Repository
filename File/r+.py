# Description:
# This program opens a file, writes text
# into it, and then reads its content.

# Step 1: Open the file in r+ mode
# r+ means we can both read and write the file
f = open(r"C:\Users\hp\OneDrive\Documents\p\File\info.txt", "r+")

# Step 2: Write text to the file
# Writing starts from the current cursor position (beginning)
f.write("Hello")    

# Step 3: Move the cursor back to the start of the file
# Without this, read() may return nothing
f.seek(0)

# Step 4: Read the file content
print(f.read())     

# Step 5: Close the file
f.close()
