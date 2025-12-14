<#
Name: Liam Saunders
Student Number: L00187849
Date: 08 Dec 2025
Task: Introduction to Switch
Description:
This script demonstrates how the PowerShell switch statement evaluates a 
value and executes a matching block of instructions. Switch branching 
is commonly used when comparing one variable against multiple possible values.
#>

# -------------------------------------------------------------------------
# Switch statement for day of the week
$DayNumber = 1

switch ($DayNumber) {
    0  { $DayName = 'Sunday'    }
    1  { $DayName = 'Monday'    }
    2  { $DayName = 'Tuesday'   }
    3  { $DayName = 'Wednesday' }
    4  { $DayName = 'Thursday'  }
    5  { $DayName = 'Friday'    }
    6  { $DayName = 'Saturday'  }
}

$DayName

# -------------------------------------------------------------------------
# Switch statement for month of the year
$MonthNumber = 12

switch ($MonthNumber) {
    1  { $MonthName = 'January'   }
    2  { $MonthName = 'February'  }
    3  { $MonthName = 'March'     }
    4  { $MonthName = 'April'     }
    5  { $MonthName = 'May'       }
    6  { $MonthName = 'June'      }
    7  { $MonthName = 'July'      }
    8  { $MonthName = 'August'    }
    9  { $MonthName = 'September' }
    10 { $MonthName = 'October'   }
    11 { $MonthName = 'November'  }
    12 { $MonthName = 'December'  }
}

$MonthName
