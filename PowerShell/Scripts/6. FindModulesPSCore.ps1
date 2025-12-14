<#
Name: Liam Saunders
Student Number: L00187849
Date: 05 Dec 2024
Task: A script to find modules which support PowerShell Core. Includes an additional command to display the total number of modules.
Note: This command may take some time to run.
#>

# Find modules that explicitly support PowerShell Core
$PGSM = Find-Module -Name * -Tag 'PSEdition_Core'
"There are {0:N0} modules that support PowerShell Core." -f $PGSM.Count

# Optional command to list all available modules
# Get-Module -ListAvailable
