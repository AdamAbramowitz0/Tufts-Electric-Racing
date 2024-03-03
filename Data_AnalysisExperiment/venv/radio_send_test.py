
import RPi.GPIO as GPIO
import time
import serial
import board
import adafruit_bno055
i2c = board.I2C()

sensor = adafruit_bno055.BNO055_I2C(i2c)
ser = serial.Serial('/dev/ttyS0', 57600, timeout = 500)

print(ser.name)
while True:
    try:
        x, y, z = sensor.linear_acceleration
        ex, ey, ez = sensor.euler
        print(ex, ey, ez)

        ser.write(int.to_bytes(int(abs(x)), 4))

        ser.write(int.to_bytes(int(abs(ex)), 4))
        ser.write(int.to_bytes(int(abs(ey)), 4))
        ser.write(int.to_bytes(int(abs(ez)), 4))

        time.sleep(.01)
    except Exception as e:
        print("ERROR HERE: "+ str(e))
        sensor = adafruit_bno055.BNO055_I2C(i2c)
	

gpio.cleanup()
