# Python File Handling - Note Saver

This project demonstrates how Python works with files.

## Concepts Covered

- Opening files
- Writing to files
- Reading from files
- Append mode
- Exception handling with files

## Features

- Save notes to a file
- Read saved notes
- Handle missing file errors

## Example

```python
with open("example.txt", "w") as file:
    file.write("Hello world")