from nicegui import run, ui
import pandas 
import requests
from queue import Queue
import threading
import datetime
import time

numberOfSensors = 1
sensorArray = ["TIMER?"]
theQueue = []
keepRunning = True
bitsPerSecond = 100000
list1 = []
list2 = []
lock = threading.Lock()
#df = pandas.DataFrame(data={'col1': list1, 'col2': list2})

#ui.table.from_pandas(df).classes('max-h-40')

line_plot = ui.line_plot(n=numberOfSensors, limit=20, figsize=(15,10), update_every=1).with_legend(sensorArray, loc='upper center')

 

def updateGraph(iteration, milis):
    #lock.acquire()
    line_plot.push(iteration,[milis])
    #lock.release()
    #print("done")


        
def fillQueue():
    iterations = []
    seconds = []
    iteration = 0

    while(keepRunning):
        #print("HIT")
        iteration+=1
        
        second = datetime.datetime.now().strftime("%f") 

        iterations.append(float(iteration))
        seconds.append(float(second))
        #print("opened")
        if(iteration%bitsPerSecond == 0):
            threading.Thread(target = updateGraph, args=(iterations, seconds)).start()
            iterations.clear()
            seconds.clear()
        
        time.sleep(float(1/bitsPerSecond))






def updateFunc():
    global keepRunning
    keepRunning = False


ui.button('Update', on_click = lambda: updateFunc())
threading.Thread(target = fillQueue).start()
ui.run()



#@ui.refreshable
#def createTable():
#    test = ui.table.from_pandas(df)

#def updateDF():
  #  global df
 #   df = pandas.DataFrame(data={'col1': [5,6,7,8,9,9,20], 'col2': [5,6,7,8,9,9,20]})

   # createTable.refresh()
   
#createTable()

#ui.button('Update', on_click = lambda: updateGraph())
#ui.button('Select all', on_click=lambda: grid.run_grid_method('selectAll'))







