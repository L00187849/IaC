"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating how functions can return multiple values using a tuple.
"""

def analyse_number(x):
    """
    Returns:
    - the number itself
    - its square
    - whether it is even (True/False)
    """
    square = x * x
    is_even = (x % 2 == 0)
    return x, square, is_even

number, square_value, even_flag = analyse_number(8)

print(f"Number: {number}")
print(f"Square: {square_value}")
print(f"Is even?: {even_flag}")
