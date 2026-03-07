# Ask user for password
password = input("Enter password: ")

strength = 0

# Check password length
if len(password) >= 8:
    strength += 1

# Variables for checks
upper = False
digit = False
special = False

# Loop through characters
for char in password:

    if char.isupper():
        upper = True

    if char.isdigit():
        digit = True

    if not char.isalnum():
        special = True


# Add strength points
if upper:
    strength += 1

if digit:
    strength += 1

if special:
    strength += 1


# Final result
if strength == 4:
    print("Strong password")

elif strength == 3:
    print("Medium password")

else:
    print("Weak password")