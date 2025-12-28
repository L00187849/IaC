"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating tuple iteration and tuple unpacking in a for-loop.
"""

# A list containing three tuples
list_of_tuples = [(1, 2), (3, 4), ("A", "B")]

# First, print each tuple as a whole
print("Printing each tuple as a single item:")
for item in list_of_tuples:
    print(item)

print("\nPrinting each value separately using tuple unpacking:")
# Now unpack each tuple into two variables, a and b
for a, b in list_of_tuples:
    print(a)
    print(b)
