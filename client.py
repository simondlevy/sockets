#!/usr/bin/env python3
'''
Server script for simple client/server example

Copyright (C) Simon D. Levy 2021

MIT License
'''
from threading import Thread
from time import sleep
import socket
from sys import stdout

from common import ADDR, PORT

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
    t.setDaemon(True)
    t.start()

    while True:
        try:
            print(data[0])
            sleep(.01)
        except KeyboardInterrupt:
            break

main()
