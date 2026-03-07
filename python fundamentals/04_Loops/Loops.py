"""
Python Loops Demonstration

This script demonstrates how loops work in Python.
It includes examples of both 'for' and 'while' loops.
"""

# -------------------------------
# Example 1: Using a for loop
# -------------------------------

print("Example 1: Printing numbers from 1 to 5 using a for loop")

# range(1,6) generates numbers from 1 to 5
for number in range(1, 6):
    print(number)


# -------------------------------
# Example 2: Using a while loop
# -------------------------------

print("\nExample 2: Countdown using a while loop")

count = 5

# Loop continues while the condition is True
while count > 0:
    print("Countdown:", count)
    count -= 1  # decrease the value by 1

print("Liftoff!")


# -------------------------------
# Example 3: Loop through a list
# -------------------------------

print("\nExample 3: Iterating through a list")

languages = ["Python", "Java", "C++", "JavaScript"]

for language in languages:
    print("Programming language:", language)