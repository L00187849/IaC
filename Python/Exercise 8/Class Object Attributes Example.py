"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate the use of class object attributes which are
    shared by all instances of a class.
"""

# -------------------------------------------------
# Class definition
# -------------------------------------------------
class MyTemplate():
    """
    A class demonstrating class-level attributes and
    instance-level attributes.
    """

    # Class object attributes (shared by all instances)
    class_object_attribute1 = 6378137
    class_object_attribute2 = 6356752

    # Constructor
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")

        # Instance attributes
        self.attr1 = attribute1
        self.attr2 = attribute2


# -------------------------------------------------
# Instantiate the class
# -------------------------------------------------
my_object = MyTemplate("Liam", True)

# -------------------------------------------------
# Access class object attributes via the instance
# -------------------------------------------------
print(
    my_object.class_object_attribute1,
    my_object.class_object_attribute2
)
