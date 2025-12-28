"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-15
Version: 1.0
Purpose: Demonstrating search in a list with proper boolean return values.
         Shows why a function can return None if no explicit return is given,
         and how to fix it by returning False when no match is found.
"""

def find_num(number_list: list[int], number: int) -> bool:
    """
    Searches for a number in a list.

    Parameters:
        number_list (list[int]): List of integers to search.
        number (int): The integer to look for.

    Returns:
        bool: True if the number is found, False otherwise.
    """
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            # No action needed here, continue checking the rest of the list
            pass

    # If we get here, the number was not found
    return False


# Example from the notes
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)  # Expected: False
