"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Start a TCP server on localhost and echo back any received messages.
    2) Demonstrate reliable, connection-based communication using TCP.
"""

import socket
import settings.tcp as settings

TCP_IP = settings.TCP["SERVER_TCP_IPv4"]
TCP_PORT = settings.TCP["SERVER_PORT"]
BUFFER_SIZE = 1024

print(f"This is the TCP server. Listening on {TCP_IP}:{TCP_PORT} (from settings/tcp.py).")
print("Press CTRL+C to stop.")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Allow quick restart without 'address already in use' errors
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind and listen
        server_socket.bind((TCP_IP, TCP_PORT))
        server_socket.listen(1)
        print(f"Bound to {TCP_IP}:{TCP_PORT}")

        while True:
            # Wait for a client connection
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connection address: {addr}")

                # Receive data from client
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    print("No data received. Closing connection.")
                    continue

                message = data.decode("utf-8", errors="replace")
                print(f"Received: {message}")

                # Echo back to client
                conn.sendall(data)

except KeyboardInterrupt:
    print("\nServer stopped by user (CTRL+C).")
except socket.error as e:
    print(f"Socket error: {e}")
