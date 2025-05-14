#2. Using cls
#Assignment:
#Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.
class Counter:
    count = 0     # class variable to keep track of the count
    def __init__(self):
        Counter.count += 1    # increment the count when a new object is created
    @classmethod
    def display_count(cls):
         return f"Total objects created: {cls.count}" # class method to display the count
        
# Create instances of Counter
count1:Counter = Counter()
count2:Counter = Counter()    
count3:Counter = Counter()
count4:Counter = Counter()
# Display the count of objects created

print(Counter.display_count())  # Output: Total objects created: 3