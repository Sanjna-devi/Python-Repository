# Store university and student details using a nested dictionary
university = {
    "Name": "Mehran university of engineering and technology",
    "student": {
        "Name": "Sanjna",
        "Rollno": "25SW066"
    }
}

# Print the entire university dictionary
print(university)

# Print only the student details
print(university["student"])

# Access and print the student's roll number
print(university["student"]["Rollno"])

