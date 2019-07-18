import os
from socket import *
import pickle
host = ""
contacts = ["10.68.107.45","10.68.104.104"]
port = 5000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
print("Waiting to receive messages...")


while True:
    rec, addr = UDPSock.recvfrom(buf)
    rec = pickle.loads(rec)
    data = rec[0]
    selfadrs = rec[1]
    if(selfadrs == contacts[0]):
        addr = (contacts[1], port)
        UDPSock.sendto(data, addr)
    elif(selfadrs == contacts[1]):
        addr = (contacts[0], port)
        UDPSock.sendto(data, port)




UDPSock.close()
os._exit(0)
