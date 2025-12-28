# Name: Liam Saunders
# Student Number: L00187849
# Purpose: Demonstrating the use of named placeholders with the .format() method.

# Store message components
a = "Good"
b = "morning"
c = "Liam"

# Using named arguments in .format() allows us to control the order of output.
# The placeholder names (first, second, third) correspond to the keyword arguments.
print("Message is: {first} {third} {second}".format(first=a, second=c, third=b))
