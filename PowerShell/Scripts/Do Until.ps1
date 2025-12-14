<#
Name: Liam Saunders
Student Number: L00187849
Date: 08 Dec 2025
Task: Creating a Do-Until loop in PowerShell
#>

# Initialise variable
$Value = 2

do {
    Write-Output "Starting loop with the number $Value"
    Write-Output $Value

    # Increment the variable by 2
    $Value += 2

    Write-Output "Now the value is $Value"

} until ($Value -ge 20)
