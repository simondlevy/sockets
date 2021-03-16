#!/usr/bin/env python3

from threading import Thread
from time import sleep
import socket
from sys import stdout

ADDR = '137.113.118.68' # Change for actual deployment
PORT = 20003

def comms(data):

    # Connect to the client
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ADDR, PORT))

    while True:

        data[0] = sock.recv(1)

        sleep(0.001) # Yield to the main thread

def main():
        
    data = [0]

    t = Thread(target=comms, args=(data,))
    t.start()

    while True:
        print(data[0])
        sleep(1)

main()
