"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Provide a function to cube a number.
    Demonstrate the use of the __name__ dunder variable to distinguish
    between running as a standalone script and being imported as a module.
"""

# --------------------------------------------------------------
# cube.py
# Contains a function to cube a number
# --------------------------------------------------------------

# A simple message related to this module
cube_text = "Yo, time to cube stuff!"


def cube(x: int) -> int:
    """
    Return the cube of the given integer.
    """
    return x * x * x


# --------------------------------------------------------------
# Module execution check
# --------------------------------------------------------------
if __name__ == "__main__":
    # This code only runs when cube.py is executed directly
    print(f"This module is called {__name__} and executes as a standalone script")
    print("Test result:", cube(2))
else:
    # This code runs when cube.py is imported by another script
    print(f"This module is called {__name__} and is being called by another script")

