<#
Name: Liam Saunders
Student Number: L00187849
Date: 08 Dec 2025
Task: Introduction to if and elseif
Description:
Conditional branching 
#>


# Basic IF example
$ValueA = 32
$ValueB = 32

if ($ValueA -ne $ValueB) {
    Write-Output "The condition was true"
}

# -------------------------------------------------------------------------
# IF / ELSEIF example using days of the week
$DayNumber = 3

if     ($DayNumber -eq 0) { $DayName = 'Sunday'    }
elseif ($DayNumber -eq 1) { $DayName = 'Monday'    }
elseif ($DayNumber -eq 2) { $DayName = 'Tuesday'   }
elseif ($DayNumber -eq 3) { $DayName = 'Wednesday' }
elseif ($DayNumber -eq 4) { $DayName = 'Thursday'  }
elseif ($DayNumber -eq 5) { $DayName = 'Friday'    }
elseif ($DayNumber -eq 6) { $DayName = 'Saturday'  }

$DayName

# -------------------------------------------------------------------------
# Using -like to match patterns
$MyName = "Liam"

if ($MyName -like "Lia*") {
    Write-Output "That's my nickname"
}

# -------------------------------------------------------------------------
# Using user input with multiple conditional checks
<#
This example accepts user input, checks whether it matches the first letters
of the author's name or the lecturer’s initials, and outputs an appropriate
response.
#>

$UserInput = Read-Host "Please enter the creator's name: "

if ($UserInput -like "Lia*") {
    Write-Output "That's the Student!"
}
elseif ($UserInput -like "JOR*") {
    Write-Output "That's the lecturer!"
}
