"""
Python Functions Project

This script demonstrates how functions work in Python.
The program calculates Body Mass Index (BMI) using a function.
"""

# -----------------------------
# Function definition
# -----------------------------

def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula:
    BMI = weight / (height^2)

    Parameters:
    weight (float): weight in kilograms
    height (float): height in meters

    Returns:
    float: calculated BMI value
    """
    bmi = weight / (height ** 2)
    return bmi


# -----------------------------
# Function to classify BMI
# -----------------------------

def bmi_category(bmi):
    """
    Determine BMI category based on BMI value
    """

    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# -----------------------------
# Main program
# -----------------------------

print("BMI Calculator")

# User input
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# Function call
bmi_value = calculate_bmi(weight, height)

# Determine category
category = bmi_category(bmi_value)

# Output results
print("\nYour BMI:", round(bmi_value, 2))
print("Category:", category)