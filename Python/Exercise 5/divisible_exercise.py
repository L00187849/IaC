"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-15
Version: 1.0
Purpose: Demonstrating a simple function that checks if one integer
         is exactly divisible by another using the modulus operator.
"""

def divisible(numerator: int, denominator: int) -> bool:
    """
    Returns True if numerator is exactly divisible by denominator.

    Parameters:
        numerator (int): The number being divided.
        denominator (int): The number we are dividing by.

    Returns:
        bool: True if numerator % denominator == 0, otherwise False.
    """
    return numerator % denominator == 0


# Test example from the notes
print(divisible(30, 4))  # Expected: False
