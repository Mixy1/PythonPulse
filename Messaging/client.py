import sys
import os
import pickle
from socket import *
# Save as client.py
# Message Sender

host = "10.68.104.104"  # set to IP address of target computer
port = 5000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
buf = 1024


while True:      
    data = input("Enter message to send or type 'exit': ").encode()

    if data.decode().lower() == "exit":
        break

    UDPSock.sendto(data, addr)

    

    (data, addr) = UDPSock.recvfrom(buf)
    print(data.decode())

#Done



UDPSock.close()
os._exit(0)
