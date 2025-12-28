"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Using a list comprehension with a condition to filter even numbers.
"""

# Build a list of even numbers from 0 to 19
evens = [x for x in range(20) if x % 2 == 0]

print("Even numbers from 0–19:")
print(evens)
