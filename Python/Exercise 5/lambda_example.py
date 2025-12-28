"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-15
Version: 1.0
Purpose: Demonstrating the use of lambda expressions for simple,
         single-use functions such as calculating circumference
         and area based on a radius.
"""

# Lambda functions for basic geometry
circumference = lambda radius: 2 * 3.142 * radius
area = lambda radius: 3.142 * radius * radius

radius = 5

print(f"Circumference for radius {radius}: {circumference(radius)}")
print(f"Area for radius {radius}: {area(radius)}")
