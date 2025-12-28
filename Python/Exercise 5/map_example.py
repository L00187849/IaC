"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-15
Version: 1.0
Purpose: Demonstrating the use of the map() function to apply a function
         to every item in an iterable without writing a manual loop.
"""

def double_number(n: int) -> int:
    """
    Simple function to double a number.

    Parameters:
        n (int): The integer to double.

    Returns:
        int: The doubled value.
    """
    return n + n


# List of values for testing
my_numbers = [1, 2, 3, 4, 5]

# Apply the function using map()
result = map(double_number, my_numbers)

# Convert to a list for display
print("List form of map result:")
print(list(result))

print("\nIterating through map directly:")
for item in map(double_number, my_numbers):
    print(item)
