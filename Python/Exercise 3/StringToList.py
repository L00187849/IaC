"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating how to convert a string into a list using .split().
         The script takes a comma-separated string and splits it into a list
         where each comma represents a separation point.
"""

# Original comma-separated string
my_string = "12/9/22, 14:30, System Start, UB2204-Server"

# Convert the string to a list by splitting at each comma
list_of_values = my_string.split(",")

# Print the resulting list
print(list_of_values)
