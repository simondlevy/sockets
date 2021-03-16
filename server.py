#!/usr/bin/env python3

import socket
from time import sleep

ADDR = '137.113.118.68' # Change for actual deployment
PORT = 20003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ADDR, PORT))
sock.listen(1) # become a server socket, maximum 1 connection

while True:

    print('Server listening on %s:%d ... ' % (ADDR, PORT))

    # This will block (wait) until a client connets
    conn, addr = sock.accept()

    print('Got a connection!')

    while True:

        try:
            conn.send('A'.encode('utf8'))
        except:
            print('Client quit')
            break;

        sleep(.01)
