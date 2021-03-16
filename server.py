#!/usr/bin/env python3
'''
Server script for simple client/server example

Copyright (C) Simon D. Levy 2021

MIT License
'''
import socket
from time import sleep

ADDR = '137.113.118.68' # Change for actual deployment
PORT = 20003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ADDR, PORT))
sock.listen(1) # become a server socket, maximum 1 connection

while True:

    try:

        print('Server listening on %s:%d ... ' % (ADDR, PORT))

        # This will block (wait) until a client connets
        conn, addr = sock.accept()

        print('Got a connection!')

    except KeyboardInterrupt: 
        break


    while True:

        try:
            conn.send('A'.encode('utf8'))
            sleep(.01)

        except Exception:
            print('Client quit')
            break;

