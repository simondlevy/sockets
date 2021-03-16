#!/usr/bin/env python3

from threading import Thread
from time import sleep
import socket

ADDR = '137.113.118.68' # Change for actual deployment
PORT = 20003

def comms(data):

    # Connect to the client
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ADDR, PORT))

    while True:

        print(sock.recv(1))

        sleep(0.1) # Yield to the main thread
        
if __name__ == '__main__':

    # Connect to the client
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ADDR, PORT))

    while True:

        print(sock.recv(1))

        sleep(0.1) # Yield to the main thread
 
    data = [0]

    t = Thread(target=comms, args=(data,))
    t.start()

    while True:
        sleep(1)
