# Hybrid inheritance
# Hybrid inheritance combines multiple and multilevel inheritance.
class A:    
    #Base class.  
    def show(self):
        print("Class A")

class B(A):
#Child of A (part of multilevel chain).
    pass

class C(A):
    #Another child of A (part of multiple inheritance).
    pass

class D(B, C):
    #Child of B and C (demonstrates hybrid inheritance).
    pass

# Creating an object of 
d = D()

# Calling a method. Python uses MRO to find the first occurrence of 'show'
d.show()
