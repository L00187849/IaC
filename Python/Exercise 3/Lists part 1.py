"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating basic list operations, including length, slicing, 
         and accessing elements using negative indexing.
"""

# A list containing integers and a single string element
my_list = [1, 2, 3, 4, "A"]

# Find and print the length of the list
a = len(my_list)
print(a)

# Slice the list from index 1 up to (but not including) index 3
slice_1 = my_list[1:3]
print(slice_1)

# Access the last element in the list using negative indexing
my_character = my_list[-1]
print(my_character)
