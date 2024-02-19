import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.animation import FuncAnimation


class handleGraph:
        def __init__(self, sensors, frequencies, largestFreq, dictionary):
                self.sensors = sensors
                self.frequencies = frequencies
                self.largestFreq = largestFreq
                self.dictionary = dictionary
        
        def startUpPlot(self):
                global fig, ax, z
                fig,ax = plt.subplots()
                ax.set_ylim(0,400)
                ax.set_xlim(0,1)
                z = []
                for i in range(0,len(self.sensors)):
                        z.append(ax.plot([],[], linewidth = 1, alpha=.8)[0])
                        z[-1:][0].set_label(self.sensors[i])
                self.runGraph()
         
                
        def runGraph(self):
                print("HIT")
                garbageCollectionStopper = FuncAnimation(fig = fig,func = self.update, frames = 1000000, interval =200, blit=False)
                plt.show()
        
        def update(self):
                ax.set_xlim(self.dictionary["time"][-1:][0]-10,self.dictionary["time"][-1:][0]+2,auto=False)

                for q in range(0,len(z)):
                        #with lock:
                        z[q].set_data(self.dictionary["time"],self.dictionary[self.sensors[q]])
                        #z[q].set_data([0,1,2],[0,1,2])

                return z