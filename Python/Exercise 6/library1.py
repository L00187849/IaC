"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate using the Python Standard Library by importing the
    entire math module and accessing sqrt via the math namespace.
"""

# --------------------------------------------------------------
# library1.py
# Demonstrates using math.sqrt() through the module namespace
# --------------------------------------------------------------

import math   # Import the full math library

print("Input lengths of the two short triangle sides:")

# Read user inputs and convert them to floating point numbers
a = float(input("a: "))
b = float(input("b: "))

# Calculate the hypotenuse using Pythagoras' theorem
c = math.sqrt(a**2 + b**2)

# Print the result formatted to 4 decimal places
print("The length of the hypotenuse to four places is: {hypo:1.4f}".format(hypo=c))
