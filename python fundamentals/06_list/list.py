"""
Python Lists Project

This script demonstrates how lists work in Python by creating
a simple To-Do List Manager. Users can add, view, and remove tasks.
"""

# List to store tasks
tasks = []

while True:
    print("\n--- To-Do List Manager ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    # View tasks
    if choice == "1":
        if len(tasks) == 0:
            print("Your task list is empty.")
        else:
            print("\nYour tasks:")
            for index, task in enumerate(tasks, start=1):
                print(index, "-", task)

    # Add a task
    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully.")

    # Remove a task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(index, "-", task)

            number = int(input("Enter task number to remove: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Removed task:", removed)
            else:
                print("Invalid task number.")

    # Exit program
    elif choice == "4":
        print("Exiting To-Do List Manager...")
        break

    else:
        print("Invalid choice. Please try again.")