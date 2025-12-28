"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating break, continue, and pass inside a for-loop.
"""

my_list = [1, 2, 3, 0]

for my_number in my_list:
    # pass: do nothing when the value is 1
    if my_number == 1:
        pass

    # continue: skip the rest of the loop body when the value is 2
    if my_number == 2:
        continue

    # Print a message when the value is 3
    if my_number == 3:
        print(f"Found the number {my_number}")

    # break: exit the loop completely when the value is 0
    if my_number == 0:
        break
