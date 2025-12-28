"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Import device classes from devices.py
    2) Create instances (objects) and test methods
"""

from devices import Firewall, Switch, LoadBalancer

# Create firewall instances and test methods
firewall27 = Firewall("firewall27")
firewall27.configure_firewall()

firewall28 = Firewall("firewall28")
firewall28.calculate_crc("dummy data")

# Create a switch instance and test methods
switch01 = Switch("switch01")
switch01.configure_switch()

# Create a load balancer instance and test methods
lb01 = LoadBalancer("lb01")
lb01.configure_load_balancer()
