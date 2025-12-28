"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-15
Version: 1.0
Purpose: Demonstrating the use of type hints and return values in a function.
         This function calculates the circumference of a circle using a
         provided radius.
"""

def calculate_circumference(radius: float) -> float:
    """
    Calculates the circumference of a circle.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: The circumference, using the formula C = 2 * π * r.
    """
    return radius * 2 * 3.142   # π approximated as 3.142


# Test the function
print(calculate_circumference(5))
