"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Detect the operating system the script is running on.
    Demonstrate:
        1) Use of the Python standard library (platform module)
        2) Functions returning values
        3) Conditional logic (if / elif / else)
        4) The __name__ == "__main__" execution pattern
"""

# --------------------------------------------------------------
# Import required standard library
# --------------------------------------------------------------
import platform


def detect_os() -> str:
    """
    Detect and return the operating system name.

    Returns:
        str: Name of the operating system
    """
    return platform.system()


# --------------------------------------------------------------
# Main execution block
# --------------------------------------------------------------
if __name__ == "__main__":
    # This block runs only when the script is executed directly
    print(f"This module is called {__name__} and executes as a standalone script")

    # Detect OS and normalise to lowercase for comparison
    my_os = detect_os()
    my_os = my_os.lower()

    # Determine OS type
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    elif my_os == "darwin":
        print("Your Apple system is MacOS")
    elif my_os == "cygwin":
        print("Your system is Windows (Cygwin)")
    elif my_os == "aix":
        print("Your IBM system is AIX")
    else:
        print(f"Unidentified system = {my_os}")

else:
    # This block runs when the script is imported as a module
    print(f"This module is called {__name__} and is being called by another script")
