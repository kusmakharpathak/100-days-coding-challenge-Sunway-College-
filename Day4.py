"""
Author :   Kusmakhar Pathak
Created:   30 July 2020
(c) Copyright by Kusmakhar Pathak.
"""

# Programme to get hostname and host IP address
import socket

# function to access host computer IP address
def get_ipAddress():
    host_pc = socket.gethostname()
    IPAddress = socket.gethostbyname(host_pc)
    return host_pc, IPAddress

print(f"The host name of host computer is : {get_ipAddress()[0]}")
print(f"The host IP address of host computer is : {get_ipAddress()[1]}")
