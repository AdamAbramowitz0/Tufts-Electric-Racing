import time
import serial

ser = serial.Serial('/dev/tty.usbserial-B001QT7U', 57600, timeout = 500)


print(ser.name)
while True:
        

