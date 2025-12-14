<#
Name: Liam Saunders
Student Number: L00187849
Date: 05 Dec 2024
Task: Pre-requisite for upgrading to PowerShell 7
#>

# Check the existing PowerShell version
$PSVersionTable

# Set an execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force

# Install NuGet as a package provider
Install-PackageProvider NuGet -MinimumVersion 2.8.5.201 -Force | Out-Null

# Install the PowerShellGet module
Install-Module -Name PowerShellGet -Force -AllowClobber

# Create a script directory
mkdir C:\PowerShell
