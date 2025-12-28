"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate the anatomy of a simple Python class,
    including a constructor, attributes, methods,
    and multiple instances.
"""

# -------------------------------------------------
# Create a class (CamelCase by convention)
# -------------------------------------------------
class LiamClass():

    # Constructor: runs when an object is created
    def __init__(self, greeting):
        print("Running constructor for LiamClass")
        # Instance attribute
        self.message = greeting

    # Method belonging to the class
    def show_message(self):
        print(self.message)


# -------------------------------------------------
# Create and use the first object
# -------------------------------------------------
my_class1 = LiamClass("Good morning Liam!")
my_class1.show_message()

# -------------------------------------------------
# Create and use the second object
# -------------------------------------------------
my_class2 = LiamClass("Hello again from MyClass2!")
my_class2.show_message()

# -------------------------------------------------
# Show the type of the object
# -------------------------------------------------
print(type(my_class1))
