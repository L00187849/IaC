"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Log CPU count and CPU load once per second to a CSV file.
    2) Demonstrate file handling, looping, and reusable utilities.
"""

from time import sleep
from file_utilities import path_name, log_file_name
from os_utilities import detect_os, cpu_load


# Check the OS and build logfile path + filename
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".csv")
full_path = log_path + filename

print(f"Detected OS: {this_os}")
print(f"Logging to: {full_path}")
print("Press Ctrl+C to stop.")


# Loop forever
while True:
    try:
        # Sleep for 1 second
        sleep(1)

        # Timestamp for this line (no extension)
        timestamp = log_file_name("")

        # CPU info (tuple)
        cpu_count, cpu_percent = cpu_load()

        # CSV line: timestamp,cpu_count,cpu_percent
        logline = f"{timestamp},{cpu_count},{cpu_percent}\n"

        # Append to logfile
        with open(full_path, "a", encoding="utf-8") as file_handle:
            file_handle.write(logline)

        print(f"Logged: {timestamp} {cpu_count} {cpu_percent}")

    except KeyboardInterrupt:
        print("\nStopped by user (Ctrl+C).")
        break

    except Exception as err:
        print(f"Error: {err}")
        break
