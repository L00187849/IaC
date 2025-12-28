"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Provide a simple object-oriented class template that can be
    reused as a starting point for future Python projects.

Revision History:
    15-DEC-2024: Initial version
"""

# -------------------------------------------------
# Class definition (CamelCase by convention)
# -------------------------------------------------
class MyTemplate():
    """
    A basic class template demonstrating:
    - Class structure
    - Constructor
    - Instance attributes
    """

    # Constructor, called whenever an instance of the class is created
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")

        # Assign arguments to instance attributes
        self.attr1 = attribute1
        self.attr2 = attribute2


# -------------------------------------------------
# Instantiate the class
# -------------------------------------------------
my_object = MyTemplate("Liam", True)

# -------------------------------------------------
# Verify object type and attributes
# -------------------------------------------------
print(type(my_object))
print(f"Attribute 1: {my_object.attr1}")
print(f"Attribute 2: {my_object.attr2}")
