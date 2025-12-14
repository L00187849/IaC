<#
Name: Liam Saunders
Student Number: L00187849
Date: 08 Dec 2025
Task: Creating a piped command in PowerShell
Description:
This script demonstrates how pipeline operators allow the output of one 
command to become the input of the next.#>

# Piping directory contents into a formatted table and sending output to the host
Dir | Format-Table | Out-Host

