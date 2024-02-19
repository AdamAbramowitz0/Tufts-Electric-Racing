import socket

class handleWeb:
        def __init__(self, arrayOfBytes,frequencyHz):
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.arrayOfBytes = arrayOfBytes
                self.frequencyHz = frequencyHz
                self.socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        def tryToEstablishSocket(self):
                global runnable
                try:
                        self.socket.connect(("localhost", 8084))

                        self.socket.sendall(bytes([len(self.arrayOfBytes)]))

                        for i in range(0,len(self.arrayOfBytes)):
                                self.socket.sendall(bytes([len(self.arrayOfBytes[i])]))
                                self.socket.sendall(self.arrayOfBytes[i])
                                self.socket.sendall(bytes([int(self.frequencyHz[i]/256)]))
                                self.socket.sendall(bytes([self.frequencyHz[i]%256]))
                except:
                        runnable = False
                        print("Cannot connect to server!")
        def sendData(self, z, rand): 
                if(runnable):
                        print(z)
                        print(self.arrayOfBytes[z])
                        print([len(self.arrayOfBytes[z])])
                        self.socket.sendall(bytes([len(self.arrayOfBytes[z])]))
                        self.socket.sendall(self.arrayOfBytes[z])
                        self.socket.sendall(bytes([int(rand)]))
                else:
                        ...