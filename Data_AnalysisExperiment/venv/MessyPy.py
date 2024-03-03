import socket
import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from decimal import *
import threading
import time
import serial

lock = threading.Lock()

ser = serial.Serial('/dev/tty.usbserial-B001QT7U', 57600, timeout = 500)


#USER SETS THE FOLLOWING
#List of sensors
sensors = ["Thing 1","Thing 2","Thing 3","Thing 4"]
frequencyHz = [100,100,100,100]
largestFreq = 100

#############

    
#GLOBAL VARIABLES THAT PROBABLY SHOULDNT EXIST
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dictionary = {}


#line2, = ax.plot([],[])
#line3, = ax.plot([],[]) 
#############

#Decimal Setup
getcontext().prec = 6
#############



def main():
    fillDictionaryWithZeros()
    
    freqThread = threading.Thread(target= getAndShowData)
    
    freqThread.start()
    initilizeGraph()
    freqThread.join()


def updateGraph(t, ax,plots):
    timeLowerBound = dictionary["time"][-1] - 10
    timeUpperbound = dictionary["time"][-1] + 2

    ax.set_xlim(timeLowerBound, timeUpperbound, auto=False)

    for plot, sensor in zip(plots, sensors):
        #with lock:
       plot.set_data(dictionary["time"], dictionary[sensor])
            #z[q].set_data([0,1,2],[0,1,2])
     
    return plots


def initilizeGraph():
    plots = []
    fig,ax = plt.subplots()
    ax.set_ylim(0,370)
    ax.set_xlim(0,1)
    for i in range(0,len(sensors)):
        plots.append(ax.plot([],[], linewidth = 1, alpha=.8)[0])
        plots[i].set_label(sensors[i])
    ax.legend()
    
    print("Starting graph animation.")
    garbageCollectionStopper = FuncAnimation(fig = fig,func = updateGraph, fargs=(ax,plots), frames = 1000000, interval =200, blit=False)
    plt.show()

def fillDictionaryWithZeros():
        global dictionary
        for i in sensors:
            dictionary[i] = [0]
        dictionary["time"] = [0]

def fillDict(iteration,z,data):
    with lock:
        dictionary[sensors[z]].append(data)
        dictionary["time"].append(Decimal(iteration)/Decimal(largestFreq))
        for i in sensors:
            if(i != sensors[z]):
                dictionary[i].append(dictionary[i][-1:][0])


def tryToEstablishSocket(runnable):
    try:

        #mySocket.setConnectionTimeout(500000)
        mySocket.connect(("localhost", 8084))
        
        mySocket.sendall(bytes([len(frequencyHz)]))

        for i in range(0,len(arrayOfBytes)):
            mySocket.sendall(bytes([len(frequencyHz[i])]))
            mySocket.sendall(bytes(frequencyHz[i],'utf-8'))
            mySocket.sendall(bytes([int(frequencyHz[i]/256)]))
            mySocket.sendall(bytes([frequencyHz[i]%256]))
        return True
    except:
        print("Cannot connect to server!")
        return False


def sendData(index, value, runnable): 
    if(runnable):

        mySocket.sendall(bytes([len(frequencyHz[index])]))
        mySocket.sendall(bytes(frequencyHz[i],'utf-8'))
        mySocket.sendall(bytes([int(value)]))


def getAndShowData():
    runnable = True
    iteration = 0
    while iteration < 20000:
        
        for index in range(0,len(frequencyHz)):

            if((iteration)%(float(largestFreq/frequencyHz[index])) == 0):
                if (iteration == 0) and (index == 0):
                    runnable = tryToEstablishSocket(runnable)
                #value = (iteration/(index+3)-random.randint(0,10))%150
                value =  int.from_bytes(ser.read(8), "big")
                sendData(index, value, runnable) #data curently random
                fillDict(iteration,index,value)

        iteration+=1
        time.sleep(float(1/largestFreq))    #adjust for time of for loop    
    df = pd.DataFrame.from_dict(dictionary)
    df.to_excel("ModularTest.xlsx")

main()