"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Send UDP multicast messages once per second to a multicast group.
    2) Demonstrate one-to-many distribution (multicast) without a direct connection.
"""

import socket
import time
from datetime import datetime
import settings.mc as settings

MCAST_GRP = settings.MCCLIENT["MCAST_GROUP"]
MCAST_PORT = settings.MCCLIENT["PORT"]
MCAST_IF_IP = settings.MCCLIENT["IP_ADDRESS"]

print("This is the multicast client.")
print(f"Sending to multicast group {MCAST_GRP}:{MCAST_PORT}.")
print(f"Using interface IP (from settings/mc.py): {MCAST_IF_IP}")
print("Press CTRL+C to stop.\n")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
    # Set the outgoing interface for multicast traffic
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(MCAST_IF_IP))

    # Optional: limit multicast packets to local network only (TTL=1)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

    while True:
        message_text = f"ATU {datetime.now()}"
        s.sendto(message_text.encode("utf-8"), (MCAST_GRP, MCAST_PORT))
        print(f"Sent: {message_text}")
        time.sleep(1)
