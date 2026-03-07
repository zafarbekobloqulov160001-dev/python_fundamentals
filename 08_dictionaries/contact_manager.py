"""
Python Dictionaries Project

This script demonstrates how dictionaries work in Python.
The program acts as a simple Contact Manager that stores names
and phone numbers.
"""

# Dictionary to store contacts
contacts = {}

while True:
    print("\n--- Contact Manager ---")
    print("1. View contacts")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    # View all contacts
    if choice == "1":
        if not contacts:
            print("No contacts saved.")
        else:
            print("\nSaved contacts:")
            for name, phone in contacts.items():
                print(name, ":", phone)

    # Add new contact
    elif choice == "2":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added successfully.")

    # Search for a contact
    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")

    # Delete a contact
    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    # Exit program
    elif choice == "5":
        print("Exiting Contact Manager...")
        break

    else:
        print("Invalid choice. Please try again.")