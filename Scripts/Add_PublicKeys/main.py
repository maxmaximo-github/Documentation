#!/usr/bin/env python3


from netmiko import Netmiko
from os import popen


devices_list = [
    "10.20.1.27", "10.20.1.28", "10.20.1.24", "10.20.1.34", "10.20.1.31",
    "10.20.1.44", "10.20.1.47", "10.20.1.27", "10.20.1.28", "10.20.1.29",
]

device_ssh = {
    
}

for ip in devices_list:
    ping = popen(f"ping {ip} -n 1")
    print(ping)


    