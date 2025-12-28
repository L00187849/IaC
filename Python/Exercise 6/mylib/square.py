"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Provide a function to square a number.
    Demonstrate the use of the __name__ dunder variable to distinguish
    between running as a standalone script and being imported as a module.
"""

# --------------------------------------------------------------
# square.py
# Contains a function to square a number
# --------------------------------------------------------------

# A simple message related to this module
square_text = "Yo, time to square stuff!"


def square(x: int) -> int:
    """
    Return the square of the given integer.
    """
    return x * x


# --------------------------------------------------------------
# Module execution check
# --------------------------------------------------------------
if __name__ == "__main__":
    # This code only runs when square.py is executed directly
    print(f"This module is called {__name__} and executes as a standalone script")
    print("Test result:", square(2))
else:
    # This code runs when square.py is imported by another script
    print(f"This module is called {__name__} and is being called by another script")
