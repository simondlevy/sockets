#!/usr/bin/env python3
'''
Server script for simple client/server example

Copyright (C) Simon D. Levy 2021

MIT License
'''
from threading import Thread
from time import sleep
import socket
from struct import unpack

from header import ADDR, PORT


def comms(data):
    '''
    Communications thread
    '''

    # Connect to the client
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ADDR, PORT))

    # Loop until main thread quits
    while True:

        # Receive and unpack three floating-point numbers
        data[0], data[1], data[2] = unpack('=fff', sock.recv(12))

        # Yield to the main thread
        sleep(0.001)


def main():

    # Create a list to receiver the data
    data = [0, 0, 0]

    # Start the client on its own thread
    t = Thread(target=comms, args=(data,))
    t.setDaemon(True)
    t.start()

    # Loop until user hits CTRL-C
    while True:

        try:
            print('%3.3f  %3.3f  %3.3f  ' % tuple(data))
            sleep(.01)

        except KeyboardInterrupt:
            break


main()
