"""
Python Conditions (if / elif / else)

This script demonstrates how conditional statements work in Python.
The program classifies a person based on age and determines their category.
"""

# Ask the user to enter their age
age = int(input("Enter your age: "))

# Conditional statements
# The program checks the age and prints the correct category

if age < 0:
    # Age cannot be negative
    print("Invalid age entered.")

elif age < 13:
    # Child category
    print("You are a child.")

elif age < 18:
    # Teenager category
    print("You are a teenager.")

elif age < 60:
    # Adult category
    print("You are an adult.")

else:
    # Senior category
    print("You are a senior citizen.")


# Additional example of condition
# Checking if the user is eligible to vote

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")