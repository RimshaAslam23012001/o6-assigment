# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price.
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Initialize the private attribute

    @property
    def price(self):
        """Getter for the price property."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter for the price property."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for the price property."""
        print("Deleting price...")
        del self._price

# Example usage
product = Product("Laptop", 1000)

# Access the price using the getter
print(product.price)  # Output: 1000

# Update the price using the setter
product.price = 1200
print(product.price)  # Output: 1200

# Delete the price using the deleter
del product.price

# Uncommenting the following line will raise an AttributeError
# because the _price attribute has been deleted
# print(product.price)
