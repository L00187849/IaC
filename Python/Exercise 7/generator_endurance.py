"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Calculate the remaining endurance of a diesel generator
    in minutes, while safely handling divide-by-zero and
    invalid input errors.
"""

def calculate_endurance(fuel: float, fuel_consumption: float) -> float:
    """
    Calculate remaining endurance in minutes.

    Args:
        fuel (float): Fuel remaining in litres
        fuel_consumption (float): Fuel usage in litres per minute

    Returns:
        float: Remaining endurance in minutes, or 0 if invalid
    """
    try:
        # Validate that values are numeric and positive
        if fuel < 0 or fuel_consumption < 0:
            raise ValueError("Fuel values must be positive numbers")

        # Calculate endurance
        endurance = fuel / fuel_consumption
        return endurance

    except ZeroDivisionError:
        # Raised when fuel_consumption is zero (engine idling)
        print("Error: Fuel consumption is zero, endurance cannot be calculated")
        return 0.0

    except ValueError as err:
        # Raised when invalid values are provided
        print(f"Value error: {err}")
        return 0.0

    except:
        # Catch any unexpected errors
        print("Unexpected error occurred")
        return 0.0


# -------------------------------
# Test cases
# -------------------------------
if __name__ == "__main__":
    print("Endurance:", calculate_endurance(120, 4))   # Normal case
    print("Endurance:", calculate_endurance(120, 0))   # Divide by zero
    print("Endurance:", calculate_endurance(-10, 4))   # Invalid value
