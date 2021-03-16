#!/usr/bin/env python3

import socket
from sys import stdout
from time import sleep

ADDR = '137.113.118.68' # Change for actual deployment
PORT = 20003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ADDR, PORT))
sock.listen(1) # become a server socket, maximum 1 connection

print('Server listening on %s:%d ... ' % (ADDR, PORT), end='')
stdout.flush()

while True:

    # This will block (wait) until a client connets
    conn, addr = sock.accept()

    print('\nGot a connection!')

    while True:

        conn.send('A'.encode('utf8'))

        sleep(.01)
