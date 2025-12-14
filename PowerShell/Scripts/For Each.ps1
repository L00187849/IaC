<#
Name: Liam Saunders
Student Number: L00187849
Date: 08 Dec 2025
Task: Introduction to Foreach loops
Description:
This script demonstrates how a foreach loop iterates through each element
of an array and processes the values one at a time.
#>

# Creating an array of characters
$CharacterArray = "L", "i", "a", "m"

# Looping through each element in the array
foreach ($Letter in $CharacterArray)
{
    $Letter
}
