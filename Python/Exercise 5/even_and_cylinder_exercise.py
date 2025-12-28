"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-15
Version: 1.0
Purpose: 
    1) Demonstrate a function that searches a list for an even number and
       returns True if one is found, otherwise False.
    2) Demonstrate a lambda function that calculates the volume of a cylinder.
"""

def contains_even(number_list: list[int]) -> bool:
    """
    Checks if the list contains at least one even number.

    Parameters:
        number_list (list[int]): List of integers to check.

    Returns:
        bool: True if any number in the list is even, otherwise False.
    """
    for n in number_list:
        if n % 2 == 0:
            return True
    return False


# Lambda function for the volume of a cylinder: V = π r^2 h
volume_cylinder = lambda radius, height: 3.142 * radius * radius * height


# --- Test the functions ---

numbers = [1, 3, 5, 7, 8]
print(f"List contains even number: {contains_even(numbers)}")  # Expected: True

radius = 3
height = 10
print(f"Volume of cylinder with radius {radius} and height {height}: {volume_cylinder(radius, height)}")
