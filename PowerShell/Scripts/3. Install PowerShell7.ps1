<#
Name: Liam Saunders
Student Number: L00187849
Date: 05 Dec 2024
Task: A script to install PowerShell 7
#>

$MYPARAMS = @{
    UseMSI                = $true
    Quiet                 = $true
    AddExplorerContextMenu = $true
    EnablePSRemoting      = $true
}

C:\PowerShell\Install-PowerShell.ps1 @MYPARAMS
