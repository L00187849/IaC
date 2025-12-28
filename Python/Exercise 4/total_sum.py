"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating how to sum values in a list using a for-loop.
"""

iterable_variable = [1, 2, 3, 4, 5, 6]

# Variable to hold the running total
total = 0

# Add each item in the list to total
for item in iterable_variable:
    total = total + item

# Print the final total after the loop finishes
print(total)
