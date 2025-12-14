<#
Name: Liam Saunders
Student Number: L00187849
Date: 08 Dec 2025
Task: Introduction to Types
#>

# Demonstrating string behaviour
$StringValue = "Hello Testing Testing!"
$StringValue.ToUpper()
$StringValue.ToLower()

# Demonstrating array types in PowerShell
$MyArray = 1, 2, 3, 4, 5
$MyArray[1]    # Shows the second element (index begins at 0)

# Example using implicit integer typing
$LittleNumber = 12345
$LittleNumber.GetType()

# Example using a large integer that PowerShell automatically treats as Int64
$BigNumber = 123456789123456789
$BigNumber.GetType()

# Demonstrating floating-point types
[float]$Float32 = 12.12
$Float32.GetType()

[double]$Float64 = 12345.1234
$Float64.GetType()
