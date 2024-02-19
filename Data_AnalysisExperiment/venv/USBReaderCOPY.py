import serial
import time

PAYLOAD_SIZE = 4

sensors = ["Linear Acceleration", "Euler 1", "Euler 2", "Euler 3"]
frequencyHz = [100,100,100,100]
largestFreq = 100
print("HIT")
ser = serial.Serial(port='/dev/tty.usbserial-B001QT7U', baudrate=57600, timeout=5, bytesize=8)
# ser = serial.Serial('/dev/tty.usbserial-B001QT7U', 57600, timeout = 500)

print("HIT")
payload:bytes = ser.read(PAYLOAD_SIZE)

intFromPacket:int = int.from_bytes(payload, byteorder='big')
print(intFromPacket)

def main():
        setUpDataframe()






##WRITING TO SPREADSHEET##
      

#Initializes first element in pandas dataframe to be zero. Is necessary for
#writing to the dataframe.
def setUpDataframe():
        global dictionary
        for i in sensors:
            dictionary[i] = [0]
        dictionary["time"] = [0]