import board
import busio
import adafruit_ssd1306
import adafruit_bno055
import digitalio
import time
import spidev
from PIL import Image,ImageDraw, ImageFont

WIDTH  = 128
HEIGHT = 64
BORDER = 5

bus = 0
device = 1

##i2c = busio.I2C(board.SCL, board.SDA)

spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz=500_000
spi.mode=0

reset_pin = digitalio.DigitalInOut(board.D0)
DC = digitalio.DigitalInOut(board.CE1) # I have no fucking idea what pin this is supposed to be, hardware wise, 
# but you can't instnatiate the SSD1306 object w/o it.
CS = digitalio.DigitalInOut(board.CE0)


#cictuirpython micropython library conflict here: spi has no attribute try_lock
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, reset_pin, CS)

oled.fill(0)
oled.show()


while True:
    image = Image.new("1", (oled.width, oled.height))

    draw = ImageDraw.Draw(image)

    oled.image(image)
    oled.show()
    time.sleep(0.1)
    oled.fill(255)
