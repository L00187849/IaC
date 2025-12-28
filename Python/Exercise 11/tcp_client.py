"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Connect to a TCP server and send a timestamp message once per second.
    2) Receive and print the echoed response from the server.
"""

import socket
import time
from datetime import datetime
import settings.tcp as settings

TCP_IP = settings.TCP["SERVER_TCP_IPv4"]
TCP_PORT = settings.TCP["SERVER_PORT"]
BUFFER_SIZE = 1024

print(f"This is the TCP client. It will connect to {TCP_IP}:{TCP_PORT} (from settings/tcp.py).")
print("Press CTRL+C to stop.")

try:
    while True:
        print(f"Trying to open a socket to {TCP_IP}:{TCP_PORT}")

        # Create a TCP socket and connect
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            message_text = f"ATU {datetime.now()}"
            message_bytes = message_text.encode("utf-8")

            # Connect, send, then wait for echo
            client_socket.connect((TCP_IP, TCP_PORT))
            client_socket.sendall(message_bytes)
            print(f"Sent: {message_text}")

            data = client_socket.recv(BUFFER_SIZE)
            print("Server echoed:", data.decode("utf-8", errors="replace"))

        time.sleep(1)

except KeyboardInterrupt:
    print("\nClient stopped by user (CTRL+C).")
except socket.error as e:
    print(f"Socket error: {e}")
