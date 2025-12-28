"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate raising an exception when user input
    does not meet validation rules.
"""

# Take an input number as a string and convert it to an integer
my_value = int(input("Enter an integer greater than 0: "))

# Validate the input
if my_value <= 0:
    # Raise an exception if the rule is broken
    raise Exception("Values must be greater than 0")
else:
    # Input passed validation
    print("Validation checks passed")
