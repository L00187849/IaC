"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate importing specific modules from a custom package (mylib),
    using aliases, and calling their functions and variables.
"""

# --------------------------------------------------------------
# project2.py
# Imports mylib.cube and mylib.square and uses them with aliases
# --------------------------------------------------------------

import mylib.cube as mycube
import mylib.square as mysquare

# Use the text and functions from the cube module
print(mycube.cube_text, mycube.cube(3))

# Use the text and functions from the square module
print(mysquare.square_text, mysquare.square(3))
