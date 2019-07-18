import sys
import os
import pickle
from socket import *
# Save as client.py
# Message Sender

host = "10.62.14.218"  # set to IP address of target computer
port = 5000
selfadrs = "10.68.107.45"
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

buf = 1024


while True:      
    data = input("Enter message to send or type 'exit': ").encode()

    if data.decode().lower() == "exit":
        break
    send = [data,selfadrs]
    send = pickle.dumps(send)
    UDPSock.sendto(send,addr)

    
    rec, addr = UDPSock.recvfrom(buf)
    rec = pickle.loads(rec)
    data = rec[0]
    print(data.decode())

#Done



UDPSock.close()
os._exit(0)
