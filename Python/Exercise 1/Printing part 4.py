# Name: Liam Saunders
# Student Number: L00187849
# Purpose: Demonstrating division and floating-point formatting in Python.

# Store values
Number = 12345
Divisor = 333

# Perform division (floating-point result)
Result = Number / Divisor

# Show full precision using .format()
print("Result of {} divided by {} is {}".format(Number, Divisor, Result))

# Limit the output to 4 decimal places using {:.4f}
print("Limiting to a float with 4 decimal places would give {:.4f}".format(Result))
