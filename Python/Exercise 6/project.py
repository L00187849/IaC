"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate how to import a custom module (reusable.py)
    and call a function from that module.
"""

# --------------------------------------------------------------
# project.py
# Demonstrates importing and using a function from reusable.py
# --------------------------------------------------------------


# Import the reusable module (file must be in the same folder)
import reusable


# Inform the user that the script has started
print("Running code from the project")

# Call the function in reusable.py and print the returned value
print(reusable.my_square(4))
