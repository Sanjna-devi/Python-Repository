# Description:
# This program writes text to a file and then
# reads it to display the content.

# Step 1: Open the file in write mode ("w")
# This will create the file if it doesn't exist,
# or overwrite it if it already exists
f=open(r"C:\Users\hp\OneDrive\Documents\python\File\data.txt","w")
f.write("I am a softwAre enginneer student building my sills in python")

# Step 2: Open the file in read mode ("r") to display its content
f=open(r"C:\Users\hp\OneDrive\Documents\python\File\data.txt","r")
print(f.read())

f.close()