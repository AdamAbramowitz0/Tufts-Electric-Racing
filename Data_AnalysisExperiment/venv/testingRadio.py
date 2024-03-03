import time
import serial

ser = serial.Serial('COM3', 57600, timeout = 500)


print(ser.name)
while True:
        
        print(int.from_bytes(ser.read(4), "big"))
        time.sleep(1)
