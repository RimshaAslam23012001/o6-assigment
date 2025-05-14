# 🧠 Python OOP Practice Assignments

This repository contains 21 beginner-to-intermediate level Object-Oriented Programming (OOP) assignments in Python, each demonstrating a specific concept through a simple class-based implementation.

---

## ✅ Assignment List

### 1. Using `self`
Create a `Student` class with `name` and `marks` attributes. Use `self` to initialize and a `display()` method to print student details.

### 2. Using `cls`
Create a `Counter` class that uses a class variable to track how many objects are created using a class method.

### 3. Public Variables and Methods
Define a `Car` class with a public `brand` variable and `start()` method. Access both from outside the class.

### 4. Class Variables and Class Methods
Create a `Bank` class with a class variable `bank_name` and a class method to change it.

### 5. Static Variables and Static Methods
Define a class `MathUtils` with a static method `add(a, b)` that returns the sum of two numbers.

### 6. Constructors and Destructors
Create a `Logger` class that prints messages when an object is created and destroyed.

### 7. Access Modifiers
Define an `Employee` class with:
- public variable `name`
- protected variable `_salary`
- private variable `__ssn`

Try accessing all three.

### 8. The `super()` Function
Create a `Person` class with a name. Inherit a `Teacher` class from it, adding a `subject` field and using `super()`.

### 9. Abstract Classes and Methods
Use the `abc` module to define an abstract class `Shape` with an abstract method `area()`. Implement it in a `Rectangle` class.

### 10. Instance Methods
Create a `Dog` class with `name` and `breed`, and a method `bark()` that uses `self`.

### 11. Class Methods
Create a `Book` class with a class variable `total_books` and a class method to increment it.

### 12. Static Methods
Create a `TemperatureConverter` class with a static method `celsius_to_fahrenheit(c)`.

### 13. Composition
Create classes `Engine` and `Car`, where `Car` takes an `Engine` object during initialization and calls its method.

### 14. Aggregation
Create classes `Department` and `Employee`. A `Department` stores a reference to an external `Employee` object.

### 15. Method Resolution Order (MRO)
Define classes A, B(A), C(A), D(B, C). Override `show()` in each and observe MRO by calling `D().show()`.

### 16. Function Decorators
Write a function decorator `log_function_call` that logs before executing `say_hello()`.

### 17. Class Decorators
Create a class decorator `add_greeting` that adds a `greet()` method returning `"Hello from Decorator!"` to a class.

### 18. Property Decorators
Create a `Product` class with private `_price`. Use:
- `@property` to get it
- `@price.setter` to update
- `@price.deleter` to delete it

### 19. `callable()` and `__call__()`
Create a `Multiplier` class with a `__call__()` method to multiply an input by a factor. Test it using `callable()`.

### 20. Creating a Custom Exception
Create a custom exception `InvalidAgeError`. Raise it from `check_age(age)` if age is less than 18. Handle it with `try...except`.

### 21. Custom Iterable Class
Create a `Countdown` class that implements `__iter__()` and `__next__()` to count down from a start number to 0 using a for-loop.

---

