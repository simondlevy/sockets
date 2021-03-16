from threading import Thread
from time import sleep
import socket

ADDR = '137.113.118.68' # Change for actual deployment
PORT = 20003

def comms(data):

    k = 0

    while True:

        data[0] = k

        k += 1

        sleep(0.1) # Yield to the main thread
        
if __name__ == '__main__':

    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ADDR, PORT))

    while True:
        sleep(1)
        print('Client has connected')
    
    #sock.send('hello')

    '''
    data = [0]

    t = Thread(target=comms, args=(data,))
    
    t.start()

    for k in range(5):
        print(data[0])
        sleep(0.5)
    '''
