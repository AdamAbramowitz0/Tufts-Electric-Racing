# mainLoop.py
# this is inteded to be the file run by our pi when it is installed in the car
import time
import serial
import board
import RPi.GPIO as GPIO
import busio
from adafruit_bus_device.i2c_device import I2CDevice

# for displays
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# wheel accelerometers
from adafruit_bno08x.i2c import BNO08X_I2C
from adafruit_bno08x import BNO_REPORT_ACCELEROMETER

# ADCs
from MCP342x import MCP342x # TODO: install?


# init (loops until success)
while(True):
    try:
        # I2C network:
        i2c = busio.I2C(board.SCL, board.SDA)
        # I2C Switch
        TCA9543A_ADDR = 0b1110_0000 # this is for writing; set last addr bit to 1 for reading
        I2C_Switch = I2CDevice(i2c, TCA9543A_ADDR)
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
        DISPLAY_HEIGHT = 64
        DISPLAY_WIDTH = 128
        WHITE = 255
        BLACK = 0
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        spi_reset_pin = digitalio.DigitalInOut(board.D4) # any pin!
        spi_cs_pin = digitalio.DigitalInOut(board.D5)    # any pin! TODO NEED 2 chip selects, 1 PER DISPLAY?
        spi_dc_pin = digitalio.DigitalInOut(board.D6)    # any pin!
        oled = adafruit_ssd1306.SSD1306_SPI(DISPLAY_WIDTH, DISPLAY_HEIGHT, spi, spi_dc_pin, spi_reset_pin, spi_cs_pin)
        font = ImageFont.load_default()

        # GPIO pins:
        # GPIO 12 - pump 1
        # GPIO 13 - pump 2
        # GPIO 14 - radio
        # GPIO 15 - radio
        # GPIO 26 - Battery Charge
        # Temperature?

        # other set up:
        # Radio misc.
        # IMU zero-ing via initial measurements, possibly

        break # everything init'd without breaking
    except Exception as e:
        print(e)


def I2CSwitch_channel(channel):
    with I2C_Switch as device:
        device.write(bytes([channel]))

# MAIN LOOP
while True:
    try:
        ############# PERIPHERALS ################
            # pumps
            # fans
            # break lights
            # horn

        ############## DISPLAYS #################
        #clear display
        oled.fill(BLACK)
        oled.show()
        # draw shit for displaying
        img = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(img)
            # draw.rectangle or whatever
        oled.image(img)
        oled.show()

        # send whatever to radio
    except Exception as e:
        print(e)





# # TCA9543A default address


# # Channel selection
# CHANNEL_0 = 0b00000001  # Enable channel 0
# CHANNEL_1 = 0b00000010  # Enable channel 1

# # Setup I2C
# i2c = busio.I2C(board.SCL, board.SDA)

# # Initialize TCA9543A
# tca9543a = I2CDevice(i2c, TCA9543A_I2C_ADDR)

# def select_channel(channel):
#     with tca9543a as device:
#         device.write(bytes([channel]))

# # Example usage
# select_channel(CHANNEL_0)
# print("Channel 0 selected.")

# # To switch to Channel 1, you would call:
# # select_channel(CHANNEL_1)
# # print("Channel 1 selected.")
