#!/usr/bin/python3
""" This module creates a class, 'myList'
    This module creates a class, 'myList'
    This module creates a class, 'myList'
"""

class MyList(list):
    """
    MyList class that inherits from the built-in list class and adds additional functionality.
    This class is designed to represent a list with an added method to print the list in sorted order.
    """

    def __init__(self):
        """
        Initializes an instance of the MyList class.

        Inherits from the built-in list class and does not require any specific initialization.
        """
        super().__init__()  # Initialize the parent class (list)

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        Uses Python's built-in sorted() function to sort the list and prints the sorted result
        without modifying the original list order.
        """
        print(sorted(self))
