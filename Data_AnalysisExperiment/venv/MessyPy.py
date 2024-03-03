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


#SETUP
SENSORS = ["Thing 1","Thing 2","Thing 3","Thing 4"]
FREQUENCYHZ = [100,100,100,100]
LARGESTFREQ = 100
TIMETORUN = 20 #Seconds
MYSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dictionary = {}

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

    for plot, sensor in zip(plots, SENSORS

):
        #with lock:
       plot.set_data(dictionary["time"], dictionary[sensor])
            #z[q].set_data([0,1,2],[0,1,2])
     
    return plots

def initilizeGraph(dataDict):
    plots = []
    fig,ax = plt.subplots()
    ax.set_ylim(0,370)
    ax.set_xlim(0,1)
    for i in range(0,len(SENSORS)):
        plots.append(ax.plot([],[], linewidth = 1, alpha=.8)[0])
        plots[i].set_label(SENSORS[i])

    ax.legend()
    
    print("Starting graph animation.")
    garbageCollectionStopper = FuncAnimation(fig = fig,func = updateGraph, fargs=(ax,plots, dataDict), frames = 1000000, interval =200, blit=False)
    plt.show()

def fillDictionaryWithZeros():
        global dictionary
        for i in SENSORS:
            dictionary[i] = [0]
        dictionary["time"] = [0]

def fillDict(iteration,z,data):
    with lock:
        dictionary[SENSORS[z]].append(data)
        dictionary["time"].append(Decimal(iteration)/Decimal(LARGESTFREQ))
        for i in SENSORS:
            if(i != SENSORS[z]):
                dictionary[i].append(dictionary[i][-1:][0])





def getAndShowData():
    iteration = 0
    while iteration < TIMETORUN * LARGESTFREQ:
        for index in range(0,len(FREQUENCYHZ)):
            if((iteration)%(float(LARGESTFREQ/FREQUENCYHZ[index])) == 0): #checks with frequency
                value =  int.from_bytes(ser.read(4), "big")
                fillDict(iteration,index,value)

        iteration+=1
        time.sleep(float(1/LARGESTFREQ))    #adjust for time of for loop    
    df = pd.DataFrame.from_dict(dictionary)
    df.to_excel("ModularTest.xlsx")
    df.to_csv("CSVForRobi.csv")



main()




# DO NOT DELETE BELOW!

# def tryToEstablishSocket(runnable):
#     try:

#         #MYSOCKET.setConnectionTimeout(500000)
#         MYSOCKET.connect(("localhost", 8084))
        
#         MYSOCKET.sendall(bytes([len(FREQUENCYHZ)]))

#         for i in range(0,len(SENSORS)):
#             MYSOCKET.sendall(bytes([len(FREQUENCYHZ[i])]))
#             MYSOCKET.sendall(bytes(FREQUENCYHZ[i],'utf-8'))
#             MYSOCKET.sendall(bytes([int(FREQUENCYHZ[i]/256)]))
#             MYSOCKET.sendall(bytes([FREQUENCYHZ[i]%256]))
#         return True
#     except:
#         print("Cannot connect to server!")
#         return False


# def sendData(index, value, runnable): 
#     if(runnable):

#         MYSOCKET.sendall(bytes([len(FREQUENCYHZ[index])]))
#         MYSOCKET.sendall(bytes(FREQUENCYHZ[index],'utf-8'))
#         MYSOCKET.sendall(bytes([int(value)]))