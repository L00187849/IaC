"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate importing a custom package (mylib) and accessing a
    package-level variable defined in __init__.py.
"""

# --------------------------------------------------------------
# project1.py
# Imports the mylib package and prints the package copyright
# --------------------------------------------------------------

import mylib  # Import the package

# Print the copyright string defined in mylib/__init__.py
print(mylib.copyright)
