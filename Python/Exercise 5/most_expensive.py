"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-15
Version: 1.0
Purpose: Using tuple unpacking and iteration to identify the most expensive
         item in a price list. Demonstrates returning multiple values from
         a function and unpacking them.
"""

def most_expensive(price_list):
    """
    Iterate through a list of (description, price) tuples
    and return the item with the highest price.

    Parameters:
        price_list (list[tuple[str, float]]): A list where each item is
                                              a tuple containing a product
                                              name and its price.

    Returns:
        tuple[str, float]: The name of the most expensive item and its price.
    """

    # Set up the variables
    max_price = 0
    max_price_item = ""

    # Iterate through each (description, price) tuple
    for description, price in price_list:
        if price > max_price:
            max_price = price
            max_price_item = description
        else:
            pass  # Placeholder for clarity

    # Return the item name AND its price
    return max_price_item, max_price


# Data to process
price_list = [
    ("Pineapple", 1.0),
    ("Apples", 0.5),
    ("Pears", 0.7),
    ("Peaches", 0.8)
]

# Unpack the returned tuple
product, price = most_expensive(price_list)

print(product, price)
