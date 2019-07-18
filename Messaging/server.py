import os
from pynput.keyboard import Key, Controller
from socket import *
import pickle
host = ""
port = 5000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")


while True:
    (data, addr) = UDPSock.recvfrom(buf)
    data = data.decode()

    print("Received message: " + str(data))




UDPSock.close()
os._exit(0)
