<#
Name: Liam Saunders
Student Number: L00187849
Date: 05 Dec 2024
Task: A script to find modules in PowerShell
Note: This command may take some time to run depending on network and repository response.
#>

$PGSM = Find-Module -Name *
"There are {0:N0} modules in the PowerShell Gallery." -f $PGSM.Count
