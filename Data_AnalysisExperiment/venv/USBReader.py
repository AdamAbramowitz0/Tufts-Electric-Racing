import socket
import time
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.animation import FuncAnimation
import pandas as pd
from decimal import *
import multiprocessing

import threading
lock = threading.Lock()



#USER SETS THE FOLLOWING
sensors = ["Temperature","Moisture","Wheel Speed","Ride Height"]
arrayOfBytes = [bytes("Temperature",'utf-8'),bytes("Moisture",'utf-8'),bytes("Wheel Speed",'utf-8'),bytes("Ride Height",'utf-8')]
frequencyHz = [1000,1,10,50]
largestFreq = 1000

#############

    
#GLOBAL VARIABLES THAT PROBABLY SHOULDNT EXIST
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
runnable = True
dictionary = {}
fig,ax = plt.subplots()
ax.set_ylim(0,150)
ax.set_xlim(0,1)
z = []

for i in range(0,len(sensors)):
    z.append(ax.plot([],[], linewidth = 1, alpha=.8)[0])
    z[-1:][0].set_label(sensors[i])
ax.legend()
print(z)
#line2, = ax.plot([],[])
#line3, = ax.plot([],[]) 
#############

#Decimal Setup
getcontext().prec = 6
#############



def main():
    fillDictionaryWithZeros()
    
    #freqSender()
    freqThread = threading.Thread(target= freqSender)
    print("HERE")
    freqThread.start()
    mapRunner()
    freqThread.join()
def initFunction():
    return z

def update(t):
    ax.set_xlim(dictionary["time"][-1:][0]-10,dictionary["time"][-1:][0]+2,auto=False)

    for q in range(0,len(z)):
        #with lock:
        z[q].set_data(dictionary["time"],dictionary[sensors[q]])
            #z[q].set_data([0,1,2],[0,1,2])
     
    return z


def mapRunner():
    print("HIT")
    garbageCollectionStopper = FuncAnimation(fig = fig,func = update, frames = 1000000, interval =200, blit=False)
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


def tryToEstablishSocket():
    global runnable
    try:
        mySocket.connect(("localhost", 8084))

        mySocket.sendall(bytes([len(arrayOfBytes)]))

        for i in range(0,len(arrayOfBytes)):
            mySocket.sendall(bytes([len(arrayOfBytes[i])]))
            mySocket.sendall(arrayOfBytes[i])
            mySocket.sendall(bytes([int(frequencyHz[i]/256)]))
            mySocket.sendall(bytes([frequencyHz[i]%256]))
    except:
        runnable = False
        print("Cannot connect to server!")

def sendData(iteration, z, rand): 
    if(runnable):
        print(z)
        print(arrayOfBytes[z])
        print([len(arrayOfBytes[z])])
        mySocket.sendall(bytes([len(arrayOfBytes[z])]))
        mySocket.sendall(arrayOfBytes[z])
        mySocket.sendall(bytes([int(rand)]))
    else:
        ...

#def doMatPlotStuff():

def freqSender():

    iteration = 0
    while iteration < 20000:
        
        for z in range(0,len(frequencyHz)):

            print(str(arrayOfBytes[z],'utf-8'))
            print(iteration%(float(largestFreq/frequencyHz[z])))
            if((iteration)%(float(largestFreq/frequencyHz[z])) == 0):
                if (iteration == 0) and (z == 0):
                    tryToEstablishSocket()
                    print("HIT")
                rand = (iteration/(z+3)-random.randint(0,10))%150
                sendData(iteration, z, rand) #data curently random
                fillDict(iteration,z,rand)

        iteration+=1
        time.sleep(float(1/largestFreq))    #adjust for time of for loop    
    df = pd.DataFrame.from_dict(dictionary)
    df.to_excel("ModularTest.xlsx")

main()

