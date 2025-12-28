"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating iteration over a string and using break in a loop.
"""

# Loop through each character in the string
for this_letter in "Liam Saunders":
    # Test for a specific letter (capital L)
    if this_letter == "L":
        print(f"Woo hoo, found a {this_letter}!")
        # Exit the loop as soon as the letter is found
        break
    else:
        print(f"Aww man, I didn't want a {this_letter}!")
