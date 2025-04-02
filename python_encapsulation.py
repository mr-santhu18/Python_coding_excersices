# Encapsulation in Python
'''
Encapsulation is one of the fundamental concepts of Object-Oriented Programming (OOP). It refers to the bundling of data (variables) and methods (functions) that operate on the data into a single unit called a class. Encapsulation also restricts direct access to some of an object’s components, which is useful for preventing accidental modification of data.
'''

# Key Aspects of Encapsulation
'''
1. Data Hiding
The internal representation of an object is hidden from the outside world.
Only specific methods (getters and setters) are provided to access or modify the data.
2. Access Modifiers in Python
Python does not have strict access control like other languages (e.g., Java or C++), but it provides naming conventions to indicate different levels of access:
- Public Members: Can be accessed from anywhere (self.name).
- Protected Members: Indicated by a single underscore (_name), can be accessed within the class and subclasses.
- Private Members: Indicated by a double underscore (__name), not directly accessible from outside the class.
'''

# example
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute

    # Public method to check balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Invalid withdrawal amount.")

# Creating an instance of BankAccount
account = BankAccount("123456789", 5000)

# Accessing public attributes
print(f"Account Number: {account.account_number}")

# Accessing private attributes (Incorrect way, will raise an error)
# print(account.__balance)  # AttributeError

# Accessing private attributes using a method
print(f"Balance: ₹{account.get_balance()}")

# Performing transactions
account.deposit(2000)
account.withdraw(1500)

# Trying to access private variable directly (Name Mangling workaround)
print(account._BankAccount__balance)  # Not recommended but possible

# advantages
'''
1. Data Protection: Prevents accidental modification of sensitive data.
2. Code Maintainability: Changes in implementation do not affect external code.
3. Data Integrity: Ensures that only valid operations are performed on data.
'''