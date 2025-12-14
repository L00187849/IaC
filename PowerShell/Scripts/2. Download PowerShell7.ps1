<#
Name: Liam Saunders
Student Number: L00187849
Date: 05 Dec 2024
Task: Download the PowerShell 7 installation script
#>

# Download PowerShell 7 installation script
Set-Location C:\PowerShell
$URI = "https://aka.ms/install-powershell.ps1"
Invoke-RestMethod -Uri $URI |
Out-File -FilePath C:\PowerShell\Install-PowerShell.ps1
