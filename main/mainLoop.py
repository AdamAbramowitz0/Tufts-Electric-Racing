# mainLoop.py
# this is inteded to be the file run by our pi when it is installed in the car
import time
import serial
import board
import RPi.GPIO as GPIO
import busio
import spidev


# for displays
import digitalio
from PIL import Image, ImageDraw, ImageFont


from adafruit_bno08x.i2c import BNO08X_I2C
from adafruit_bno08x import BNO_REPORT_ACCELEROMETER
import adafruit_ssd1306


# init (loops until success)
while(True):
    try:
        # I2C network:
        i2c = busio.I2C(board.SCL, board.SDA)
        # I2C switch
        # ADC on network 1
        # ADC on network 2
        # Main body IMU
        # FL wheel IMU
        # FR wheel IMU
        # BL wheel IMU
        # BR wheel IMU
        # battery box moisture sensor 1
        # battery box moisture sensor 2

        # SPI network:
        spi = spidev.SpiDev()
        # spi.open(bus, device)
        spi.max_speed_hz = 500_000
        spi.mode = 0

        # GPIO pins:
        # GPIO 12 - pump 1
        # GPIO 13 - pump 2
        # GPIO 14 - radio
        # GPIO 15 - radio
        # GPIO 26 - Battery Charge
        # Temperature?

        # other set up:
        # Radio
        # IMU zero-ing via initial measurements, possibly

        break # everything init'd without breaking
    except Exception as e:
        print(e)


# bno1.enable_feature(BNO_REPORT_ACCELEROMETER)
# bno2.enable_feature(BNO_REPORT_ACCELEROMETER)

# loop
while True:
    try:
        # get sensor data
        # handle peripherals (e.g. pumps, fans, lights, etc.)
        # update displays
        # send whatever to radio
    except Exception as e:
        print(e)