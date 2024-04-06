import board
import digitalio
import time
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 5

spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D5)
oled_cs.direction = digitalio.Direction.OUTPUT
oled_cs2 = digitalio.DigitalInOut(board.D17)
oled_dc = digitalio.DigitalInOut(board.D6)

oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)
oled2 = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs2)

# Clear display.
oled.fill(0)
oled.show()
oled2.fill(0)
oled2.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))
image2 = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
draw2 = ImageDraw.Draw(image2)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)
draw2.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)


# Draw a smaller inner rectangle
draw.rectangle(
    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
    outline=0,
    fill=0,
)
draw2.rectangle(
    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
    outline=0,
    fill=0,
)

# Load default font.
font = ImageFont.load_default()

# Draw Some Text
text = "Hello World!"
text2 = "Something Else!"
bbox = font.getbbox(text)
bbox2 = font.getbbox(text2)
(font_width, font_height) = bbox[2] - bbox[0], bbox[3] - bbox[1]
(font_width2, font_height2) = bbox2[2] - bbox2[0], bbox2[3] - bbox2[1]
draw.text(
    (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)
draw2.text(
    (oled.width // 2 - font_width2 // 2, oled.height // 2 - font_height2 // 2),
    text2,
    font=font,
    fill=255,
)


# Display image
while True:
    oled.image(image)
    oled.show()
    time.sleep(0.1)

    oled2.image(image2)
    oled2.show()

    time.sleep(0.1)
