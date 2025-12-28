"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Store multicast settings for mc_client.py and mc_server.py.
    2) Select multicast group, port, and the network interface IP to use.
"""

MCSERVER = {
    "MCAST_GROUP": "239.1.1.1",
    "IP_ADDRESS": "127.0.0.1",   # CHANGE THIS to your real LAN IP for best results
    "PORT": 5001
}

MCCLIENT = {
    "MCAST_GROUP": "239.1.1.1",
    "IP_ADDRESS": "127.0.0.1",   # CHANGE THIS to your real LAN IP for best results
    "PORT": 5001
}
