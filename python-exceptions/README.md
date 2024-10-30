# Python Exceptions

## Overview
This coursework focuses on understanding and handling exceptions in Python. We will learn how to use try-except blocks, raise exceptions, and create custom exception classes.

## Objectives
- Understand the concept of exceptions in Python.
- Learn how to handle exceptions using try-except blocks.
- Raise exceptions using the `raise` statement.
- Create and use custom exception classes.

## Topics Covered
1. **Introduction to Exceptions**
    - What are exceptions?
    - Common built-in exceptions.

2. **Handling Exceptions**
    - Using try-except blocks.
    - Multiple except clauses.
    - The else and finally clauses.

3. **Raising Exceptions**
    - Using the `raise` statement.
    - Raising built-in exceptions.
    - Raising custom exceptions.

4. **Custom Exception Classes**
    - Creating custom exceptions.
    - Using custom exceptions in your code.

## Example Code
```python
# Example of handling exceptions
try:
     result = 10 / 0
except ZeroDivisionError as e:
     print(f"Error: {e}")

# Example of raising an exception
def check_positive(number):
     if number < 0:
          raise ValueError("Number must be positive")

# Example of custom exception
class CustomError(Exception):
     pass

try:
     raise CustomError("This is a custom error")
except CustomError as e:
     print(f"Caught custom error: {e}")
```
## Resources
- [Python Documentation on Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python - Exceptions](https://realpython.com/python-exceptions/)
