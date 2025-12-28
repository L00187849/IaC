"""
Name: Liam Saunders
Student Number: L00187849
Date: 2024-12-14
Version: 1.0
Purpose: Demonstrating iteration over a dictionary and using .items()
         to access both keys and values.
"""

# A sample dictionary of IPv4 addresses and ports
scan = {
    "192.168.3.10": "80",
    "192.168.3.11": "443",
    "192.168.3.55": "22"
}

print("Iterating over scan (keys only):")
for item in scan:
    # This prints only the keys
    print(item)

print("\nIterating over scan.items() (key and value):")
for ipv4, port in scan.items():
    # This prints both the key and value, unpacked from the tuple
    print(f"Found a service on {ipv4} at {port}")
