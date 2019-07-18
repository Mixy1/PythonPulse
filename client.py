import sys
import pygame
import pickle
from socket import *
# Save as client.py
# Message Sender

def on_key_release(key):
    print('Released Key %s' % key)

def on_key_press(key):
    data = key
    print('Pressed key %s' % key)    

host = "10.68.107.45"  # set to IP address of target computer
port = 5000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
screen = pygame.display.set_mode((400, 300))
print("Enter message to send or type 'exit': ")

while True:
    data = []
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                data.append('a')
            if event.key == pygame.K_d:
                data.append('d')
            if event.key == pygame.K_w:
                data.append('w')
            if event.key == pygame.K_s:
                data.append('s')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                data.append('au')
            if event.key == pygame.K_d:
                data.append('du')
            if event.key == pygame.K_w:
                data.append('wu')
            if event.key == pygame.K_s:
                data.append('su')

    if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
    print(data)
    if(len(data) >= 1):
        data = pickle.dumps(data)
        UDPSock.sendto(data, addr)

UDPSock.close()
os._exit(0)
