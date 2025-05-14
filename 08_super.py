#8. The super() Function
#Assignment:
#Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__ (self, name):
        self.name = name
        
# Inherited class
class Teacher(Person):
    def __init__ (self, name, subject):
        super().__init__(name)  # Call the constructor of the base class
        self.subject = subject
   
# Test the Teacher class
teacher = Teacher("Ali", "Mathematics")
print(f"Name: {teacher.name}", f"Subject: {teacher.subject}")


