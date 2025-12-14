<#
Name: Liam Saunders
Student Number: L00187849
Date: 08 Dec 2025
Task: A script to calculate VAT and produce a formatted output message.
#>

# Declare the net value and VAT rate
$NET = 111
$VAT = 0.23

# Calculate VAT amount based on the net value
$VATAmount = $NET * $VAT

# Calculate the gross amount
$Gross = $NET + $VATAmount

# Create a formatted text output
$text = "The total €$Gross is the sum of the net value €$NET with the VAT amount €$VATAmount at $($VAT * 100)% VAT rate."

# Display the text
$text
