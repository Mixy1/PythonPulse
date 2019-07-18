import sys
import os
import pickle
from socket import *
# Save as client.py
# Message Sender

host = "10.62.14.218"  # set to IP address of target computer
port = 5000
selfed = "10.68.107.45"
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

buf = 1024


while True:      
    data = input("Enter message to send or type 'exit': ").encode()
    UDPSock.sendto(data, addr)

    if data.decode().lower() == "exit":
        break
    (data, addr) = UDPSock.recvfrom(buf)
    print(data.decode())

#Done



UDPSock.close()
os._exit(0)
