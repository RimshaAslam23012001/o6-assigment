#7. Access Modifiers: Public, Private, and Protected
#Assignment:
#Create a class Employee with:

#a public variable name,

#a protected variable _salary, and

#a private variable __ssn.

#Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__ (self, name, salary, ssn):
        self.name = name
        self._salary = salary # Protected variable
        self.__ssn = ssn # Private variable
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")
#Test the Employee class
employee = Employee("John Doe", 5000, "123-45-6789")
#Accessing the public variable
print(employee.name)  # Output: John Doe
#Accessing the protected variable
print(employee._salary)  # Output: 50000
#Accessing the private variable
# print(employee.__ssn)  # This will raise an AttributeError
#Accessing the private variable using name mangling
print(employee._Employee__ssn)  # Output: 123-45-6789
#The public variable name can be accessed directly.
#The protected variable _salary can be accessed directly, but it's a convention to treat it as "protected" and not access it directly outside the class.

