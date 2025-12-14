<#
Name: Liam Saunders
Student Number: L00187849
Date: 08 Dec 2025
Task: Using variables in PowerShell
#>

# Displays the list of available variables
Get-Variable

# Declaring a variable containing mixed object types (array, string, symbols)
$Mixed_Variable = 1, 2, "a", "££"
$Mixed_Variable

# Clearing a variable value
Clear-Variable -Name Mixed_Variable
$Mixed_Variable

# Removing the variable completely
Remove-Variable -Name Mixed_Variable

# Re-declaring the variable to demonstrate object typing
$Mixed_Variable = 1, 2, "a", "££"
$Mixed_Variable.GetType()

# Demonstrating a strongly typed integer variable
[int]$Mixed_Variable = 1
$Mixed_Variable

# Showing automatic type conversion when assigning a numeric string
[int]$Mixed_Variable = 1
$Mixed_Variable = "123456789"
$Mixed_Variable.GetType()

# Showing that PowerShell cannot convert alphabetic strings into integers
[int]$Mixed_Variable = 1
$Mixed_Variable = "This will give you an error!"
$Mixed_Variable

# Translating a date string into a DateTime object
[datetime]$TodayDate = "12/08/2025"
$TodayDate

# Demonstrating creation of a new read-only variable with a description
Remove-Variable LiamVariable -ErrorAction SilentlyContinue
New-Variable LiamVariable -Value 3.142 -Description "PI with write-protection" -Option ReadOnly
Get-Variable LiamVariable
