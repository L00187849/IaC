"""
Name: Liam Saunders
Student Number: L00187849
Date: 16-DEC-2025
Version: 1.0
Purpose:
    1) Demonstrate an abstract-style base class (Device) that should not be instantiated.
    2) Demonstrate inheritance with a child class (Firewall) that inherits attributes/methods.
    3) Demonstrate method overriding (calculate_crc) in the child class.
"""

# -------------------------------------------------
# Base class (abstract-style): should NOT be instantiated
# -------------------------------------------------
class Device:
    """
    Base class for network devices.
    Holds common attributes and behaviours that child classes inherit.
    """

    # Class object attribute (shared across all instances)
    pi = 3.142

    def __init__(self) -> None:
        # Constructor for base class
        print("Running constructor for base class")
        # Common attribute for all devices
        self.debug = False

    def run(self) -> None:
        """
        Abstract-style method: forces child classes to implement their own 'run'.
        """
        raise NotImplementedError("This is an abstract class, do not instantiate")

    def calculate_crc(self, frame: str) -> int:
        """
        Placeholder CRC method (base implementation).
        Child classes may override this.
        """
        print("Checking CRC from base")
        # Dummy CRC value for demonstration
        crc = 123456789
        return crc


# -------------------------------------------------
# Child class: Firewall inherits from Device
# -------------------------------------------------
class Firewall(Device):
    """
    Child class representing a firewall device.
    Inherits from Device and adds firewall-specific methods/attributes.
    """

    def __init__(self, parameter1: str) -> None:
        # Call back to the parent class constructor
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")

        # Firewall-specific attributes
        self.parameter1 = parameter1
        self.test_message = ""

    def configure_firewall(self) -> None:
        # Example firewall-specific method
        print("Configuring Firewall")

    # -------------------------------------------------
    # Override the base class method
    # -------------------------------------------------
    def calculate_crc(self, frame: str) -> int:
        """
        Override the base class calculate_crc() method.
        """
        print("Checking CRC from child")
        # Dummy CRC value for demonstration
        crc = 123456789
        return crc


# -------------------------------------------------
# Test code (runs only when executed directly)
# -------------------------------------------------
if __name__ == "__main__":
    # Demonstrate why we shouldn't instantiate the base class
    # (Uncomment to see the NotImplementedError)
    # my_device = Device()
    # my_device.calculate_crc("dummy")
    # my_device.run()

    # Create and test a Firewall instance
    hostname = "firewall3"
    my_firewall = Firewall(hostname)

    # Calls the OVERRIDDEN method in Firewall (not the base)
    my_firewall.calculate_crc("dummy")

    # Call a child-class-specific method
    my_firewall.configure_firewall()
