# 17. Class Decorators
# Assignment:
# Create a class decorator `add_greeting` that modifies a class to add a greet() method 
# returning "Hello from Decorator!". Apply it to a class `Person`.

# Define the class decorator
def add_greeting(cls):
    # Define a new method that will be added to the class
    def greet(self):
        return "Hello from Decorator!"
    
    # Attach the greet method to the class
    cls.greet = greet

    # Return the modified class
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    # Constructor to initialize name
    def __init__(self, name):
        self.name = name

    # A regular method to introduce the person
    def introduce(self):
        return f"My name is {self.name}."

# Example usage
# Create an instance of the decorated Person class
person = Person("Alice")

# Call the original method from the class
print(person.introduce())  # Output: My name is Alice.

# Call the method added by the decorator
print(person.greet())      # Output: Hello from Decorator!
