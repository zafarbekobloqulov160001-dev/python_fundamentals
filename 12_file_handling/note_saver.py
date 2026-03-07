"""
Python File Handling Project

This script demonstrates how to read from and write to files in Python.
The program allows users to save notes and read them later.
"""

# File name
file_name = "notes.txt"

while True:
    print("\n--- Note Saver ---")
    print("1. Write a note")
    print("2. Read notes")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    # Write a note to file
    if choice == "1":
        note = input("Enter your note: ")

        # Open file in append mode
        with open(file_name, "a") as file:
            file.write(note + "\n")

        print("Note saved successfully.")

    # Read notes from file
    elif choice == "2":
        try:
            with open(file_name, "r") as file:
                content = file.read()

                if content:
                    print("\nSaved Notes:")
                    print(content)
                else:
                    print("No notes found.")

        except FileNotFoundError:
            print("No notes file found yet.")

    # Exit program
    elif choice == "3":
        print("Exiting Note Saver...")
        break

    else:
        print("Invalid option. Please try again.")