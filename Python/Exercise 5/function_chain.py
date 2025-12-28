"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating one function calling another function.
"""

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def calculate_area(width, height):
    """Uses multiply() to compute the area of a rectangle."""
    return multiply(width, height)

area = calculate_area(5, 10)

print(f"The area is: {area}")
