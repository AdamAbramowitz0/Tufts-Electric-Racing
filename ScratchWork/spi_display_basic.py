import board
import busio
import adafruit_ssd1306
import digitalio
import time
from PIL import Image,ImageDraw, ImageFont

WIDTH  = 128
HEIGHT = 64
BORDER = 5

bus = 0
device = 1


spi = busio.SPI(board.SCK, MOSI=board.MOSI)
reset_pin = digitalio.DigitalInOut(board.D4) # any pin!
cs_pin = digitalio.DigitalInOut(board.D5)    # any pin!
dc_pin = digitalio.DigitalInOut(board.D6)    # any pin!

oled = adafruit_ssd1306.SSD1306_SPI(128, 32, spi, dc_pin, reset_pin, cs_pin)


while True:
    image = Image.new("1", (oled.width, oled.height))

    draw = ImageDraw.Draw(image)

    oled.image(image)
    oled.show()
    time.sleep(0.1)
    oled.fill(255)
