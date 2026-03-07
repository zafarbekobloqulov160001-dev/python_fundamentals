"""
Python Exception Handling Project

This script demonstrates how to handle errors in Python
using try, except, and finally blocks.
"""

print("Safe Calculator")

try:
    # Ask user for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Ask for operation
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        result = num1 / num2

    else:
        print("Invalid operation")
        result = None

    # Display result
    if result is not None:
        print("Result:", result)

# Handle invalid input (text instead of number)
except ValueError:
    print("Error: Please enter valid numbers.")

# Handle division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Always executed
finally:
    print("Calculator session finished.")