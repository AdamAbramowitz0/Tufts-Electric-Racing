import socket
import time
import random
#User Sets
arrayOfBytes = [bytes("Wheel-Speed",'utf-8'), bytes("Ride Height",'utf-8'), bytes("Temperature",'utf-8'),bytes("Moisture",'utf-8')]
frequencyHz = [1000,100,1,20]
largestFreq = 1000
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.connect(("localhost", 8084))

mySocket.sendall(bytes([len(arrayOfBytes)]))

for i in range(0,len(arrayOfBytes)):
    mySocket.sendall(bytes([len(arrayOfBytes[i])]))
    mySocket.sendall(arrayOfBytes[i])
    mySocket.sendall(bytes([int(frequencyHz[i]/256)]))
    mySocket.sendall(bytes([frequencyHz[i]%256]))


def freqSender():

    iteration = 0
    while True:
        for z in range(0,len(frequencyHz)):
            print(str(arrayOfBytes[z],'utf-8'))
            print(iteration%(float(largestFreq/frequencyHz[z])))
            if(iteration%(float(largestFreq/frequencyHz[z])) == 0):
                mySocket.sendall(bytes([len(arrayOfBytes[z])]))
                mySocket.sendall(arrayOfBytes[z])
                mySocket.sendall(bytes([int((iteration%235)/(1+z))]))
        iteration+=1
        time.sleep(float(1/largestFreq))    #adjust for time of for loop    


freqSender()

#Send number of sensors
#Send name of each sensor (In order of read)
#Send frequencies of each sensor
#Begin sending