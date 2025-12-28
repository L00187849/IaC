"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Provide simple reusable functions that can be imported
    into other Python scripts.
"""

# --------------------------------------------------------------
# reusable.py
# A simple module containing reusable functions
# --------------------------------------------------------------


def my_square(a: int) -> int:
    """
    Square a number and return the result.
    """

    # Inform the user that this code is running from the module
    print("Running code from the module")

    # Return the value of a multiplied by itself
    return a * a
