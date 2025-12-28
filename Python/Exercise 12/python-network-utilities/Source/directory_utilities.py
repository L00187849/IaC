"""
Name: Liam Saunders
Student Number: L00187849
Date: 01-OCT-2023
Version: 1.0
Purpose:
    Detect the OS in use and print the current working directory.
"""

import os
import platform
import sys

# Define global variables
current_working_directory = None

def detect_os() -> str:
    """Detect the OS in use."""
    return platform.system()

def detect_working_directory() -> str:
    """Return the directory this script was run from."""
    return os.getcwd()

if __name__ == '__main__':
    print("This module executes as a standalone script")

    # Check the OS in use, lower case
    my_os = detect_os().lower()

    # Parse the response, only check for Windows and Linux
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    else:
        print(f"Cannot continue, unidentified system = {my_os}")
        sys.exit(1)

    # Get the current working directory
    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")

else:
    print(f"This module is called {__name__} and is being called by another script")
