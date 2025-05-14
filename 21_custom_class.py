# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() 
# to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        # Initialize the starting number
        self.start = start
        self.current = start  # Keep track of the current number

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        # Return the current number and decrement it each time
        if self.current < 0:
            # Stop iteration when we reach below 0
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Example usage
countdown = Countdown(5)

# Using the object in a for loop (iterable behavior)
for number in countdown:
    print(number)
