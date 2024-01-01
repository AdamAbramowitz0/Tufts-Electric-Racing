import socket
import time
import random
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.connect(("localhost", 8084))


while True:
    for i in range(0,100):
        #if(i%2 == 0):
            #mySocket.sendall(bytes(str(i%2),'utf-8'))
        if(i%2 == 0):
            mySocket.sendall(bytes([i%2, random.randint(0,255)]))
        else:
            mySocket.sendall(bytes([i%2,i]))
        time.sleep(.01)
