
"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating a basic while-loop with an else clause.
         The loop increments x until it reaches 10, then the else block runs.
"""

x = 0

# While x is less than 10, print its value and increment it
while x < 10:
    print(f"X is = {x}")
    x = x + 1      # could also write: x += 1

# This runs when the loop finishes normally (no break)
else:
    print(f"As x is now = {x}, we are all finished")
