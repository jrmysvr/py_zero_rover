import time
import board
import busio
import adafruit_mpu6050

i2c = busio.I2C(board.SCL, board.SDA)
dev = adafruit_mpu6050.MPU6050(i2c, address=0x68)

while True:
    x, y, z = dev.acceleration
    print(f"\rAcceleration: X:{x:.2f}, Y: {y:.2f}, Z: {z:.2f} m/s^2", end="\r")
    time.sleep(0.1)
