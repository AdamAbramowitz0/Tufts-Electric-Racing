from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import datetime
import threading,time,json
from queue import Queue
import pandas as pd

myQueue = Queue()
lock = threading.Lock()
ws = []
rh = []
t = []
curr = []
sensors = []
class MyServerClass(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path == '/'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            testStr=""
            for i in sensors:
                testStr+="<h2>"+i+"</h2><h2 id='"+i+"'></h2>"
            myStr = "<!DOCTYPE html><html>" + testStr+"<div></div><script>runner();function runner(){console.log('HIT');const Http=new XMLHttpRequest();const url='http://localhost:8000/data';Http.open('GET',url);Http.send();Http.onreadystatechange=()=>{var myJson=JSON.parse(Http.responseText);document.getElementById(myJson['strID']).innerHTML=myJson['Value'];console.log(myJson['val']);};setTimeout(runner,10);}</script></html>"
            self.wfile.write(bytes(myStr,'utf-8'))

        elif(self.path == '/data'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")#doesent really matter here
            self.end_headers()
            while myQueue.qsize == 0:
                print("YO")
        
            z = {
                "strID": curr[0],
                "Value": str(curr[1]),
               
            }
            jsonString = json.dumps(z)
            #print(jsonString)
            self.wfile.write(bytes(jsonString,'utf-8'))
            
     

def usbListener():
    #while True:
    global curr
    global sensors
    mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mySocket.bind(("localhost",8084))
    mySocket.listen()
    theSock,retAddr = mySocket.accept()
    numSensors = theSock.recv(1)[0]
    
    freqs = []
    maxFreq = 0

    for z in range(0,numSensors):
        sizeToRec = theSock.recv(1)[0]
        print(sizeToRec)
        sensor = str(theSock.recv(sizeToRec),'utf-8')
        print(sensor)
        overflow = theSock.recv(1)[0]
        print(overflow)
        freq = overflow*256 + theSock.recv(1)[0]
        if freq > maxFreq:
            maxFreq = freq
        
        sensors.append(sensor)
        freqs.append(freq)
    dictionary = {}
    for i in sensors:
        dictionary[i] = [0]
    dictionary["time"] = [0]
    counter = 0



    threading.Thread(target = theServer.serve_forever).start()

    while counter < 5000:
        sizeToRec = theSock.recv(1)
        part = str(theSock.recv(sizeToRec[0]),'utf-8')
        value = theSock.recv(1)[0]
        dictionary[part].append(value)
        for i in sensors:
            if (i != part):
                dictionary[i].append(dictionary[i][len(dictionary[i])-1])
        dictionary["time"].append(float(counter/maxFreq))
        with lock:
            curr = [part, value]
        print(part)
        print(value)
        time.sleep(1/maxFreq)#freq/2?
        counter +=1

    df = pd.DataFrame.from_dict(dictionary)

    df.to_excel("ModularTest.xlsx")


theServer = HTTPServer(('localhost',8000),MyServerClass)

threading.Thread(target = usbListener).start()


#mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#mySocket.bind(("localhost",8084))
#mySocket.listen()
#theSock,retAddr = mySocket.accept()
#while True:
#    x = theSock.recv(8080)
#    print(x[0])
#    if(x[0] == 71):
        
   #     theSock.sendall(b'HTTP/1.1 200 OK Content-Type: text/html \n\n')
   #     theSock.sendfile(open("test.html",'rb'))

  #  else:
   #     theSock.sendall(b'1')
        


#theSock.sendfile(open("test.html",'rb'))
















