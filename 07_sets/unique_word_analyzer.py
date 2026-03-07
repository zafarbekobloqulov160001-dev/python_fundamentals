"""
Python Sets Project

This script demonstrates how sets work in Python.
The program finds unique words in a given sentence.
"""

# Ask the user to enter a sentence
text = input("Enter a sentence: ")

# Convert sentence into words
words = text.lower().split()

# Create a set to store unique words
unique_words = set(words)

# Display results
print("\nTotal words:", len(words))
print("Unique words:", len(unique_words))

print("\nList of unique words:")
for word in unique_words:
    print("-", word)


# Additional example: removing duplicate numbers

print("\nExample with numbers:")

numbers = [1, 2, 3, 3, 4, 4, 5, 6]

# Convert list to set to remove duplicates
unique_numbers = set(numbers)

print("Original list:", numbers)
print("Unique numbers:", unique_numbers)