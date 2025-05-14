#4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Allied Bank"
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
# Create instances of the Bank class
bank1: Bank = Bank()

# Access the class variable
print(bank1.bank_name)  # Output: Allied Bank

# Change the bank name using the class method
Bank.change_bank_name("National Bank")
# Access the class variable again
print(bank1.bank_name)  # Output: National Bank
