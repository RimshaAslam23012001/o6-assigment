#5. Static Variables and Static Methods
#Assignment:
#Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
#Test the static method
result = MathUtils.add(5, 3)
print(f"The sum of 5 and 3 is: {result}")