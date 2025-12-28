"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating basic Python set operations.
         This script:
         - Creates an empty set
         - Adds values to the set
         - Shows that sets automatically remove duplicates
"""

# Create an empty set
my_set = set()

# Display the type to confirm it is a set
print(type(my_set))

# Print initial (empty) set
print(my_set)

# Add values to the set
my_set.add(1)
my_set.add(2)

# Attempt to add duplicates — they will not be stored twice
my_set.add(1)
my_set.add(2)

# Print the final set
print(my_set)
