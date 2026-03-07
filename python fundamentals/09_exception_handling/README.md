# Python Exception Handling - Safe Calculator

This project demonstrates how to handle runtime errors in Python.

## Concepts Covered

- try block
- except block
- handling ValueError
- handling ZeroDivisionError
- finally block

## Features

- Prevents program crashes
- Handles invalid input
- Handles division by zero

## Example

```python
try:
    x = int(input())
except ValueError:
    print("Invalid number")