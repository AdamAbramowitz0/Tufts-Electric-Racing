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

class MyServerClass(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path == '/'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open('test.html','rb') as file:
                self.wfile.write(file.read())
        elif(self.path == '/data'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")#doesent really matter here
            self.end_headers()
            while myQueue.qsize == 0:
                print("YO")
            x = myQueue.get()
            z = {
                "wheelspeed": -1,
                "rideheight": -1,
            }
            
            if(x[0] == 0):
                z["wheelspeed"] = x[1]
            else:
                z["rideheight"] = x[1]
            jsonString = json.dumps(z)
            #print(jsonString)
            self.wfile.write(bytes(jsonString,'utf-8'))
            
     

def usbListener():
    #while True:
    global x
    print("START")
    mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mySocket.bind(("localhost",8084))
    mySocket.listen()

    theSock,retAddr = mySocket.accept()
    print("GOT HERE")
    counter = 0
    while counter < 500:
        with lock:#is this necessary for a threadsafe queue?
            x = theSock.recv(2)
            myQueue.put(x)
            #Nan
        if(x[0] == 0):
            ws.append(x[1])
            #rh.append(-1)
            #t.append(counter/2)
        elif(x[0] == 1):
            rh.append(x[1])
            t.append(counter/2)
            #ws.append(-1)
        
            #myQueue.put(theSock.recv(2))#packet-length
            #myQueue.put(theSock.recv(2)[0]), 1 rideheight 0 wheelspeed
        time.sleep(.01)#freq/2?
        counter +=1
    print(len(rh))
    print(len(ws))
    df = pd.DataFrame({
    "Wheel_Speed": ws,
    "Ride_Height": rh,
    "Time": t}
)

    df.to_excel("FinalTEST.xlsx")


theServer = HTTPServer(('localhost',8000),MyServerClass)

threading.Thread(target = theServer.serve_forever).start()
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

















