"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Send a UDP message once per second to the server address and port defined in settings/udp.py.
    2) Demonstrate that UDP is connectionless (messages can be sent even if no server is running).
"""

import socket
import time
from datetime import datetime
import settings.udp as settings

# Read settings from the settings file
UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]

# Provide user feedback
print(f"This is the UDP client. It will send packets to {UDP_IP}:{UDP_PORT} (from settings/udp.py).")
print("This script has no error handling, by design. Press CTRL+C to stop.\n")

# Loop forever until CTRL+C
while True:
    # Create a UDP socket (AF_INET = IPv4, SOCK_DGRAM = UDP)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Allow broadcast capability (not strictly needed for loopback, but matches the lecture notes)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # Build a message containing a timestamp
        message_text = f"ATU {datetime.now()}"
        message_bytes = message_text.encode("utf-8")

        # Send the UDP datagram (no connection handshake in UDP)
        s.sendto(message_bytes, (UDP_IP, UDP_PORT))

        # Print confirmation to screen
        print(f"Sent: {message_text}")

    # Wait 1 second before sending again
    time.sleep(1)
