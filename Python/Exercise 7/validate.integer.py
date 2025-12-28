"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate how to validate user input using
    try / except / else / finally by ensuring the
    user enters a valid integer value.
"""

def validate_integer():
    # Loop indefinitely until valid input is received
    while True:
        try:
            # Prompt user for input and attempt to convert to integer
            user_input = int(input("Enter an integer value: "))
        except ValueError:
            # Raised when input cannot be converted to an integer
            print("Error: That was not a valid integer.")
            continue
        else:
            # Runs only if no exception occurred
            print("Valid input received.")
            break
        finally:
            # This block always executes
            print("This message displays every time, regardless of programme flow")

# Call the function
validate_integer()
