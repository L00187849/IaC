# Name: Liam Saunders
# Student Number: L00187849
# Purpose: Demonstrating how to remove specific characters (parentheses) using strip().

# A string containing brackets around the name
text_with_brackets = "(Liam Saunders)"

# Remove the opening bracket
text_without_brackets = text_with_brackets.strip('(')

# Remove the closing bracket
text_without_brackets = text_without_brackets.strip(')')

# Display the cleaned string
print(text_without_brackets)
