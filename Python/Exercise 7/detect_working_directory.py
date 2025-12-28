"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Provide basic operating system utilities.
    1) Detect the operating system in use.
    2) Exit the program if the OS is not Windows or Linux.
    3) Detect and display the current working directory.
"""

# --------------------------------------------------------------
# Import required standard libraries
# --------------------------------------------------------------
import os
import platform
import sys


# --------------------------------------------------------------
# Global variables
# --------------------------------------------------------------
current_working_directory = None


def detect_os() -> str:
    """
    Detect and return the operating system name.

    Returns:
        str: Name of the operating system
    """
    return platform.system()


def detect_working_directory() -> str:
    """
    Detect and return the current working directory.

    Returns:
        str: Current working directory path
    """
    return os.getcwd()


# --------------------------------------------------------------
# Main execution block
# --------------------------------------------------------------
if __name__ == "__main__":
    print("This module executes as a standalone script")

    # Detect operating system and normalise to lowercase
    my_os = detect_os().lower()

    # Only allow Windows or Linux
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    else:
        print(f"Cannot continue, unidentified system = {my_os}")
        sys.exit()

    # Detect and display working directory
    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")

else:
    print(f"This module is called {__name__} and is being called by another script")
