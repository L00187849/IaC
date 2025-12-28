"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Demonstrate a parent (base) class called Device.
    2) Demonstrate a child class called Firewall inheriting from Device.
    3) Demonstrate method overriding (calculate_crc).
"""

# Parent class: holds attributes/methods common to all devices
class Device:
    # Class attribute (same value for all instances of Device and its children)
    pi = 3.142

    # Constructor: runs whenever an object is created
    def __init__(self) -> None:
        print("Running constructor for base class")
        # Instance attribute (unique per object)
        self.debug = False

    # Placeholder method: base class should not be run directly
    def run(self) -> None:
        raise NotImplementedError("This is an abstract class, do not instantiate")

    # Default CRC method (child classes can override this)
    def calculate_crc(self, frame: str) -> int:
        print("Checking CRC from base")
        # Dummy return value for demonstration
        crc = 123456789
        return crc


# Child class: Firewall inherits from Device
class Firewall(Device):

    # Constructor: runs whenever a Firewall object is created
    def __init__(self, hostname: str) -> None:
        # Call parent constructor first
        super().__init__()
        print(f"Running constructor for {hostname}")

        # Store an identifier for this firewall instance
        self.hostname = hostname
        self.test_message = ""

    # Firewall specific behaviour
    def configure_firewall(self) -> None:
        print(f"Configuring Firewall: {self.hostname}")

    # Override the base class method
    def calculate_crc(self, frame: str) -> int:
        print("Checking CRC from child")
        # Dummy return value for demonstration
        crc = 123456789
        return crc


# Additional device classes (simple examples)
class Switch(Device):
    def __init__(self, hostname: str) -> None:
        super().__init__()
        self.hostname = hostname

    def configure_switch(self) -> None:
        print(f"Configuring Switch: {self.hostname}")


class LoadBalancer(Device):
    def __init__(self, hostname: str) -> None:
        super().__init__()
        self.hostname = hostname

    def configure_load_balancer(self) -> None:
        print(f"Configuring Load Balancer: {self.hostname}")
