<#
Name: Liam Saunders
Student Number: L00187849
Date: 05 Dec 2024
Task: A script to create a custom PowerShell module and verify availability.
Note: Demonstrates module folder structure, function definition, and module discovery.
#>

# Define the module path within the user's PowerShell module directory
$MyModulePath = "C:\Users\$env:USERNAME\Documents\PowerShell\Modules\HelloWorld"

# Define the content of the module using a here-string
$MyModule = @"
# HelloWorld.psm1
Function Get-HelloWorld {
    "Hello World from Liam Saunders"
}
"@

# Create the directory if it does not already exist
New-Item -Path $MyModulePath -ItemType Directory -Force | Out-Null

# Output the module file into the correct location
$MyModule | Out-File -FilePath "$MyModulePath\HelloWorld.psm1"

# Verify that the module is available on the system
Get-Module -Name HelloWorld -ListAvailable
