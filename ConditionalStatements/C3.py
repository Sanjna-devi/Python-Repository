# Multiple Conditions Example
# Checks conditions one by one and executes the first True condition

marks=int(input("Enter obtained marks: "))

if marks>=90:
    print("A")
elif 90>marks>=80:
    print("B")
elif 80>marks>=70:
    print("C")
elif marks<70:
    print("Fail")