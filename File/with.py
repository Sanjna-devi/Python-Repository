# This program reads a file, prints its content,
# then overwrites it with new content, and
# prints the updated content.

# Step 1: Read and display the original content
with open(r"C:\Users\hp\OneDrive\Documents\python\File\intro.txt","r") as f:
    data = f.read()
    print(data)

# Step 2: Overwrite the file with new content
with open(r"C:\Users\hp\OneDrive\Documents\python\File\intro.txt","w") as f:
    data = f.write("and will graduate when i will be 21 years old")
    
# Step 3: Read and display the updated content
with open(r"C:\Users\hp\OneDrive\Documents\python\File\intro.txt", "r") as f:
    updated_data = f.read()
    print("\nUpdated Content:")
    print(updated_data)