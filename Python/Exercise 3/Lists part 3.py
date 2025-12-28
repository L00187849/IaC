"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating how to create a nested list in Python.
         Instead of concatenating the contents, this script
         stores two lists inside one larger list.
"""

# First list containing integers and a string
my_list_1 = [1, 2, 3, 4, "A"]

# Second list containing strings and integers
my_list_2 = ["S", "T", "Fish", 9, 10]

# Creating a nested list (a list containing both lists)
concatenated_list = [my_list_1, my_list_2]

# Print the nested list
print(concatenated_list)
