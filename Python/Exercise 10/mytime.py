"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate the use of the datetime module to obtain
    machine-readable and human-readable date and time values.
"""

from datetime import datetime as dt

# Get the current date and time
current_time = dt.now()
print("Current datetime object:")
print(current_time)

# Get Unix epoch time
unix_epoch_time = dt.timestamp(current_time)
print("\nUnix epoch time:")
print(unix_epoch_time)

# Human-readable date values
year = current_time.strftime("%Y")
month = current_time.strftime("%B")
day = current_time.strftime("%d")
weekday = current_time.strftime("%A")

# Human-readable time values
hours = current_time.strftime("%H")
minutes = current_time.strftime("%M")
seconds = current_time.strftime("%S")

print("\nHuman readable date:")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Weekday: {weekday}")

print("\nHuman readable time:")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
