
import serial
import time

from decimal import *

import pandas as pd
#import serial.Serial as serial
import threading
lock = threading.Lock()
getcontext().prec = 6


class handleRead:
        def __init__(self, sensors, frequencyHz, largestFreq, dictionary,sendData):
                self.sensors = sensors
                self.frequencyHz = frequencyHz
                self.largestFreq = largestFreq
                self.dictionary = dictionary
                self.sendData = sendData

        def freqSender(self):
                ser = serial.Serial('/dev/tty.usbserial-B001QT7U', 57600, timeout = 500)
                print("I AM HERE")
                iteration = 0
                while iteration < 1000:
                        for z in range(0,len(self.frequencyHz)):
                                if((iteration)%(float(self.largestFreq/self.frequencyHz[z])) == 0):
                                        value = int.from_bytes(ser.read(8),'big')                        
                                        self.sendData(iteration, z, value)
                                        self.fillDict(iteration,z,value)
                                #sendData(0, 0,serial())
                                iteration+=1
                                time.sleep(float(1/self.largestFreq))    #adjust for time of for loop    
                df = pd.DataFrame.from_dict(self.dictionary)
                df.to_excel("ModularTest.xlsx")

        def fillDict(self, iteration,z,data):
                with lock:
                        self.dictionary[self.sensors[z]].append(data)
                        self.dictionary["time"].append(Decimal(iteration)/Decimal(self.largestFreq))
                        for i in self.sensors:
                                if(i != self.sensors[z]):
                                        self.dictionary[i].append(self.dictionary[i][-1:][0])

