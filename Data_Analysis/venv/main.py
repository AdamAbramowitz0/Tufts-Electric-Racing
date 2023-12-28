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
#list1 = []
#list2 = []
#df = pandas.DataFrame(data={'col1': list1, 'col2': list2})

#ui.table.from_pandas(df).classes('max-h-40')

line_plot = ui.line_plot(n=numberOfSensors, limit=20, figsize=(15,10), update_every=1).with_legend(sensorArray, loc='upper center')



def updateGraph():
    iteration = 0
    while(keepRunning):

       
        iteration+=1
        if((not (len(theQueue)<=1))):
            line_plot.push([float(theQueue.pop())],[[float(theQueue.pop())]])
        
        time.sleep(.01)

def fillQueue():
    iteration = 0
    while(keepRunning):
        iteration+=1
        second = datetime.datetime.now().strftime("%s")
        
        theQueue.insert(0,iteration)
        theQueue.insert(0,second)
    
        time.sleep(.1)


threadReadingTime = threading.Thread(target = fillQueue)
threadUpdatingGraph = threading.Thread(target = updateGraph)




def updateFunc():
    global keepRunning
    keepRunning = False


ui.button('Update', on_click = lambda: updateFunc())

threadReadingTime.start()
threadUpdatingGraph.start()
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







