"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating basic Python dictionary operations.
         This script shows how to:
         - Create a dictionary
         - Add a new key/value pair
         - Modify an existing value
         - Print dictionary contents
"""

# Create the initial dictionary
my_dictionary = {
    "FName": "Liam",
    "SName": "Saunders",
    "Occupation": "IT Technician"
}

# Print the original dictionary
print(my_dictionary)

# Add a new key/value pair
my_dictionary["Salary"] = "Not Enough!"

# Print dictionary after adding the new pair
print(my_dictionary)

# Modify an existing key/value pair
my_dictionary["Occupation"] = "Network engineer!"

# Print final dictionary
print(my_dictionary)
