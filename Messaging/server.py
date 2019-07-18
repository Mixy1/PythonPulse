import os
from pynput.keyboard import Key, Controller
from socket import *
import pickle
host = ""
port = 5000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
UDPSock.bind(addr)
keyboard = Controller()
print("Waiting to receive messages...")


while True:
    (data, addr) = UDPSock.recvfrom(buf)
    data = pickle.loads(data)
    for dat in data:
        if(len(dat) == 1):
            keyboard.press(dat)
        elif(len(dat) > 1):
            keyboard.release(dat[:1])



    print("Received array: " + str(data))




UDPSock.close()
os._exit(0)
