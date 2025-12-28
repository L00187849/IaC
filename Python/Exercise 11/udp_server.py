"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Listen on a UDP port defined in settings/udp.py.
    2) Receive and print UDP messages sent by udp_client.py.
"""

import socket
import settings.udp as settings

# Read settings from the settings file
UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024

# Provide user feedback
print(f"This is the UDP server. It will listen on {UDP_IP}:{UDP_PORT} (from settings/udp.py).")
print("This script has no error handling, by design. Press CTRL+C to stop.\n")

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Allow broadcast capability (matches lecture notes)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Bind the socket to the IP and port (start listening)
    s.bind((UDP_IP, UDP_PORT))
    print(f"Listening on {UDP_IP}:{UDP_PORT}\n")

    # Loop forever receiving data
    while True:
        # Receive a UDP packet (data, address)
        data, addr = s.recvfrom(BUFFER_SIZE)

        # Decode bytes to string
        message_text = data.decode("utf-8", errors="replace")

        # Print sender details and message
        print(addr, message_text)
