# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError.
# Write a function check_age(age) that raises this exception if age < 18.
# Handle it with try...except.

# Define the custom exception class
class InvalidAgeError(Exception):
    """Exception raised when the provided age is invalid (i.e., less than 18)."""
    
    def __init__(self, age, message="Age must be 18 or older."):
        self.age = age
        self.message = message
        # Call the base class constructor with a custom error message
        super().__init__(f"{message} Provided age: {age}")

# Define a function that checks the age
def check_age(age):
    """Check if the age is 18 or above. Raise InvalidAgeError if not."""
    if age < 18:
        raise InvalidAgeError(age)
    print("Access granted. Age is valid.")

# Test the custom exception with try...except
try:
    # Take user input and convert it to integer
    user_age = int(input("Enter your age: "))
    
    # Call the function to check the age
    check_age(user_age)

except InvalidAgeError as e:
    # Handle the custom exception
    print("InvalidAgeError:", e)

except ValueError:
    # Handle non-integer input
    print("Please enter a valid number for age.")

