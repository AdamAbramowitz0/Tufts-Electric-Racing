import board
import busio
import time
from adafruit_bno08x.i2c import BNO08X_I2C
from adafruit_bno08x import BNO_REPORT_ACCELEROMETER

i2c = busio.I2C(board.SCL, board.SDA)

bno1 = BNO08X_I2C(i2c)
bno2 = BNO08X_I2C(i2c, address=0x4b)

while True:
    try:
        bno1.enable_feature(BNO_REPORT_ACCELEROMETER)
        bno2.enable_feature(BNO_REPORT_ACCELEROMETER)

        bno1.begin_calibration()
        bno2.begin_calibration()

        print(f"Calibration Status #1: {bno1.calibration_status}")
        print(f"Calibration Status #2: {bno2.calibration_status}")
        break
    except Exception as e:
        print(e)

print("Press q to quit, any other key to read: ")


while True:
    command = input()
    if command == "q":
        break
    try:
        print()
        x1, y1, z1 = bno1.acceleration  # pylint:disable=no-member
        x2, y2, z2 = bno2.acceleration  # pylint:disable=no-member

        print("BNO #1: X: %0.6f  Y: %0.6f Z: %0.6f  m/s^2" % (x1, y1, z1))
        print("BNO #2: X: %0.6f  Y: %0.6f Z: %0.6f  m/s^2" % (x2, y2, z2))
        print()
    except Exception as e:
        print(e)
        pass
