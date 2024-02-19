


import handleGraph
import handleWeb
import handleRead

#USER SETS THE FOLLOWING
sensors = ["Linear Acceleration", "Euler 1", "Euler 2", "Euler 3"]
arrayOfBytes = [bytes("Linear Acceleration",'utf-8'),bytes("Euler 1",'utf-8'),bytes("Euler 2",'utf-8'),bytes("Euler 3",'utf-8')]
frequencyHz = [100,100,100,100]
largestFreq = 100

#############


#GLOBAL VARIABLES THAT PROBABLY SHOULDNT EXIST

runnable = True

def main():
    global runnable
    dictionary = {}
    fillDictionaryWithZeros(dictionary)
    graphToDisplay = handleGraph(sensors, frequencyHz, largestFreq, dictionary)
    webHandler = handleWeb(arrayOfBytes,frequencyHz)
    reader = handleRead()


   
    freqThread = threading.Thread(target= freqSender)
    print("HERE")
    freqThread.start()

    
    graphToDisplay.startUpPlot()

    freqThread.join()

main()


def fillDictionaryWithZeros(dictionary):
        for i in sensors:
            dictionary[i] = [0]
        dictionary["time"] = [0]






#def doMatPlotStuff():





