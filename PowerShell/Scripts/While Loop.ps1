<#
Name: Liam Saunders
Student Number: L00187849
Date: 08 Dec 2025
Task: Introduction to While loops
#>

# -------------------------------------------------------------------------
# Example 1 – Simple While loop with numeric increment
# -------------------------------------------------------------------------

# Initialise the variable before evaluating it in the loop
$value = 0

while ($value -ne 5)
{
    $value++
    Write-Host "The value is now: $value"
}

# -------------------------------------------------------------------------
# Example 2 – While loop combined with user input and switch branching
# -------------------------------------------------------------------------

<#
This loop reads user input until the value "P" is entered. 
Each recognised letter triggers a specific output message.
#>

while (($InputValue = Read-Host -Prompt "Select a command to run (H, A, R or P):") -ne "P")
{
    switch ($InputValue)
    {
H { Write-Output "Help option selected." }
A { Write-Output "Action option selected." }
R { Write-Output "Reset option detected." }
P { Write-Output "Process termination requested." }
default { Write-Output "Input not valid. Acceptable values are H, A, R, or P." }

    }
}
