import os
from pynput.keyboard import Key, Controller
from socket import *
import pickle
host = ""
contacts = ["10.68.107.45","10.68.104.104"]
port = 5000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")


while True:
    (data, addr) = UDPSock.recvfrom(buf)
    data = data.decode()
    if(addr = contacts[0]):
        addr = (contacts[1], port)
        UDPSock.sendto(data, addr)
    elif(addr = contacts[1]):
        addr = (contacts[0], port)
        UDPSock.sendto(data, port)




UDPSock.close()
os._exit(0)
