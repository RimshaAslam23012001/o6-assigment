# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" 
# before a function executes. Apply it to a function say_hello()

# Define the decorator function
def log_function_call(func):
    # Inner wrapper function that adds additional behavior
    def wrapper(*args, **kwargs):
        # This line is executed before the actual function call
        print("Function is being called")
        # Call the original function with any arguments
        return func(*args, **kwargs)
    # Return the wrapper to replace the original function
    return wrapper

# Applying the decorator to the function say_hello
@log_function_call
def say_hello(name):
    # Function body that simply prints a greeting
    print(f"Hello, {name}!")

# Calling the decorated function
say_hello("Ali")  # This will first print the decorator message, then the greeting
