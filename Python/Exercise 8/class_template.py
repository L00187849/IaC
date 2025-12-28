"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Provide a reusable template for creating simple Python classes,
    including class attributes, instance attributes, and methods.
"""

# -------------------------------------------------
# Class definition (CamelCase by convention)
# -------------------------------------------------
class ClassTemplate():
    """
    Generic class template for reuse in future projects.
    """

    # Class object attributes (shared by all instances)
    class_object_attribute1 = "DEFAULT_VALUE_1"
    class_object_attribute2 = "DEFAULT_VALUE_2"

    # -------------------------------------------------
    # Constructor
    # -------------------------------------------------
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        """
        Constructor, runs when an object is created.

        Args:
            attribute1 (str): Name or identifier
            attribute2 (bool): Flag to control behaviour
        """
        self.attr1 = attribute1
        self.attr2 = attribute2

    # -------------------------------------------------
    # Method using object attributes
    # -------------------------------------------------
    def my_method1(self) -> None:
        """
        Uses object attributes to control output.
        """
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")

    # -------------------------------------------------
    # Method with runtime argument
    # -------------------------------------------------
    def my_method2(self, my_name: str = "User") -> None:
        """
        Uses a runtime argument with a default value.

        Args:
            my_name (str): Name to greet (optional)
        """
        if self.attr2:
            print(f"Good morning {my_name}")
        else:
            print(f"No greeting {my_name}")


# -------------------------------------------------
# Test the class when run directly
# -------------------------------------------------
if __name__ == "__main__":
    my_object = ClassTemplate("Liam", True)

    my_object.my_method1()
    my_object.my_method2("Slartibartfast")
    my_object.my_method2()
