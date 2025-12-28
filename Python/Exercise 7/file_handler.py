"""
Name: Liam Saunders
Student Number: L00187849
Date: 15DEC24
Version: 1.0
Purpose:
    Demonstrate basic file handling using:
    - with statement
    - append mode
    - structured exception handling
"""

my_filename = "logfile.txt"

try:
    # Open the file in append mode
    with open(my_filename, "a") as file_handle:
        print(f"Writing a test line to {my_filename}")
        file_handle.write("Test line\n")

except IOError as err:
    print(f"IOError was: {err}")

except EOFError as err:
    print(f"End of file error was: {err}")

except OSError:
    print("Operating System Error occurred")

except:
    print("General Error occurred")

else:
    # Runs only if no exception occurred
    print("File operation completed successfully")

finally:
    # Always runs
    print("Finishing up!")
    # No need to close file when using 'with'
