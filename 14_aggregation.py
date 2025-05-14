#14. Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

#  String representation of the Employee object
    def __str__(self):
        return f"{self.name} (ID: {self.employee_id})"

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  # Aggregation: reference to an existing Employee object

    def show_details(self):
        print(f"Department: {self.name}")
        print(f"Employee: {self.employee}")

# Create an Employee object independently
emp1 = Employee("Ali", 100)

# Create a Department object and pass the existing Employee object
dept1 = Department("Fainance", emp1)

# Display department details
dept1.show_details()



