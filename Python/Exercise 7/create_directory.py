"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 2.0
Purpose:
    Demonstrate systematic error handling using try/except.
    Handle directory creation with distinct return codes for:
        0 = directory created successfully
        1 = error creating directory
        2 = directory already exists
"""

# --------------------------------------------------------------
# Imports (standard library)
# --------------------------------------------------------------
import os
import platform
import sys


def detect_os() -> str:
    """
    Detect and return the operating system name.
    """
    return platform.system()


def detect_working_directory() -> str:
    """
    Return the directory this script was run from.
    """
    return os.getcwd()


def create_directory(directory_name: str) -> int:
    """
    Attempt to create a directory and return a status code.

    Return codes:
        0 -> Directory created successfully
        1 -> Error creating directory
        2 -> Directory already exists
    """
    # Check if the directory already exists
    if os.path.isdir(directory_name):
        return 2
    else:
        try:
            # Attempt to create the directory
            os.mkdir(directory_name)
            return 0
        except:
            print(f"Error creating directory {directory_name}")
            return 1


# --------------------------------------------------------------
# Main execution block
# --------------------------------------------------------------
if __name__ == "__main__":
    print("This module executes as a standalone script")

    # Detect OS
    my_os = detect_os().lower()

    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    else:
        print(f"Cannot continue, unidentified system = {my_os}")
        sys.exit()

    # Detect working directory
    print(f"You are coding in: {detect_working_directory()}")

    # ----------------------------------------------------------
    # Directory creation logic using return codes
    # ----------------------------------------------------------
    result = create_directory("LIAM")

    if result == 0:
        print("Creating a directory worked")
        # Do other stuff
    elif result == 1:
        print("You couldn't create a directory!")
        # Do other stuff
    elif result == 2:
        print("Directory already existed!")
        # Do other stuff

else:
    print(f"This module is called {__name__} and is being called by another script")
