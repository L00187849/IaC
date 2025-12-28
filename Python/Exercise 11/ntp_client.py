"""
Name: Liam Saunders
Student Number: L00187849
Date: 16-DEC-2024
Version: 1.0
Purpose:
    To demonstrate the use of the Network Time Protocol (NTP) in Python.
    This script queries a public NTP server using UDP and displays
    timing and synchronisation information returned by the server.
"""

import ntplib
from time import ctime

# Define the NTP server to query
ntp_server = "ie.pool.ntp.org"

# Create an NTP client instance
ntp_client = ntplib.NTPClient()

# Send request to the NTP server
ntp_response = ntp_client.request(ntp_server)

# If a response is received, display key timing information
if ntp_response:
    print(f"NTP Time: {ctime(ntp_response.tx_time)}")
    print(f"Precision: {ntp_response.precision}")
    print(f"Version: {ntp_response.version}")
    print(f"Offset: {ntp_response.offset}")
    print(f"Root delay: {ntp_response.root_delay}")
    print(f"Root dispersion: {ntp_response.root_dispersion}")
    print(f"Delay: {ntp_response.delay}")
    print(f"Leap indicator: {ntp_response.leap}")
    print(f"Stratum of NTP server: {ntp_response.stratum}")

