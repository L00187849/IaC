"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate importing only a specific function (sqrt)
    from the math module for cleaner and more efficient code.
"""

# --------------------------------------------------------------
# library2.py
# Demonstrates direct function import (sqrt) from math module
# --------------------------------------------------------------

from math import sqrt   # Import only the required function

print("Input lengths of the two short triangle sides:")

# Read user inputs and convert them to floating point numbers
a = float(input("a: "))
b = float(input("b: "))

# Calculate the hypotenuse
c = sqrt(a**2 + b**2)

# Print the formatted result
print("The length of the hypotenuse to four places is: {hypo:1.4f}".format(hypo=c))
