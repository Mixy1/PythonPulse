import sys
import os
import pickle
import multiprocessing
from socket import *
# Save as client.py
# Message Sender

host = "10.68.107.45"  # set to IP address of target computer
port = 5000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Enter message to send or type 'exit': ").encode()
    UDPSock.sendto(data, addr)

    if data.decode().lower() == "exit":
        break

UDPSock.close()
os._exit(0)
