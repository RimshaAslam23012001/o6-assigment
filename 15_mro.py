# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

# Base class A with a show() method
class A:
    def show(self):
        print("A's show() method")

# Class B inherits from A and overrides the show() method
class B(A):
    def show(self):
        print("B's show() method")

# Class C also inherits from A and overrides the show() method
class C(A):
    def show(self):
        print("C's show() method")

# Class D inherits from both B and C (Multiple Inheritance)
# and overrides the show() method
class D(B, C):
    def show(self):
        print("D's show() method")

# Create an object of class D
d = D()

# Call the show() method — this will invoke D's version
d.show()

# Print the Method Resolution Order to understand the order in which
# Python looks for methods in the inheritance hierarchy
print("Method Resolution Order (MRO):", D.__mro__)
