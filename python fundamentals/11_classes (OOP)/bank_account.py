"""
Python Classes (OOP) Project

This script demonstrates how classes and objects work in Python.
The program simulates a simple bank account system.
"""

class BankAccount:
    """
    A simple BankAccount class to demonstrate OOP concepts.
    """

    # Constructor method
    def __init__(self, owner, balance=0):
        """
        Initialize account with owner name and starting balance.
        """
        self.owner = owner
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        """
        Add money to the account.
        """
        self.balance += amount
        print(f"${amount} deposited successfully.")

    # Method to withdraw money
    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds exist.
        """
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")

    # Method to display account information
    def display_balance(self):
        """
        Show the current balance.
        """
        print(f"Account owner: {self.owner}")
        print(f"Current balance: ${self.balance}")


# -----------------------------
# Example usage
# -----------------------------

# Create a bank account object
account = BankAccount("Zafar", 100)

# Display initial balance
account.display_balance()

# Deposit money
account.deposit(50)

# Withdraw money
account.withdraw(30)

# Display final balance
account.display_balance()