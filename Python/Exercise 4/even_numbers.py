"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Using a for-loop and an if-statement to filter even numbers.
"""

iterable_variable = [1, 2, 3, 4, 5, 6]

# Loop through each number in the list
for item in iterable_variable:
    # Check if the number is even (remainder 0 when divided by 2)
    if item % 2 == 0:
        print(item)
