"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Join a multicast group and receive UDP multicast messages.
    2) Print received messages to the terminal for screenshot evidence.
"""

import socket
import settings.mc as settings

MCAST_GRP = settings.MCSERVER["MCAST_GROUP"]
MCAST_PORT = settings.MCSERVER["PORT"]
MCAST_IF_IP = settings.MCSERVER["IP_ADDRESS"]

print("This is the multicast server.")
print(f"Listening for multicast group {MCAST_GRP} on port {MCAST_PORT}.")
print(f"Interface IP (from settings/mc.py): {MCAST_IF_IP}")
print("Press CTRL+C to stop.\n")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
    # Allow reuse (helps on restarts)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to all interfaces on the chosen port
    s.bind(("", MCAST_PORT))

    # Join multicast group on the chosen interface
    # membership_request = group + interface
    membership_request = socket.inet_aton(MCAST_GRP) + socket.inet_aton(MCAST_IF_IP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership_request)

    while True:
        data, address = s.recvfrom(1024)
        message = data.decode("utf-8", errors="replace")
        print(f"Received {len(data)} bytes from {address}: {message}")
