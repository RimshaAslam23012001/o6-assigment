# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor.
# Define a __call__() method that multiplies an input by the factor.
# Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        # Initialize the multiplication factor
        self.factor = factor

    def __call__(self, x):
        # Make the object callable
        # Multiply the input x by the factor
        return x * self.factor

# Create an instance of Multiplier with a factor of 3
multiply = Multiplier(3)

# Test if the object is callable
print(callable(multiply))  # Output: True

# Call the object like a function with input 5
result = multiply(5)       # This invokes multiply.__call__(5)

# Print the result
print(result)              # Output: 15, because 5 * 3 = 15
