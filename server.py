#!/usr/bin/env python3
'''
Server script for simple client/server example

Copyright (C) Simon D. Levy 2021

MIT License
'''
import socket
from time import sleep
from struct import pack

from header import ADDR, PORT

# Serve a socket with a maximum of one client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ADDR, PORT))
sock.listen(1)

# Loop until client quits or user hits CTRL-C
while True:

    try:

        print('Server listening on %s:%d ... ' % (ADDR, PORT))

        # This will block (wait) until a client connets
        conn, addr = sock.accept()

        print('Got a connection!')

        # We'll send three arbitrary floating-point values
        a = 0.01
        b = 0.02
        c = 0.03

    except KeyboardInterrupt:
        break

    while True:

        try:

            # Pack the values into a binary array and send them
            conn.send(pack('fff', a, b, c))

            # Increase the values noticeably
            a += .01
            b += .01
            c += .01

            # Wait a briefly before sending again
            sleep(.01)

        except Exception:
            print('Client quit')
            break
