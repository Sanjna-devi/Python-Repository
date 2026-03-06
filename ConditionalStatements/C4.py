# Nested If Statement
# An if statement inside another if statement

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")   # both conditions are True
    else:
        print("License required")