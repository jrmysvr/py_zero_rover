import time
import board
import busio
from .adafruit_mma8451 import MMA8451


pl_puf = [
         "PL_PUF: Portrait, up, front",
         "PL_PUB: Portrait, up, back",
         "PL_PDF: Portrait, down, front",
         "PL_PDB: Portrait, down, back",
         "PL_LRF: Landscape, right, front",
         "PL_LRB: Landscape, right, back",
         "PL_LLF: Landscape, left, front",
         "PL_LLB: Landscape, left, back",
         ]

def init_device():
    i2c = busio.I2C(board.SCL, board.SDA)
    return MMA8451(i2c, address=0x1d)

def track_acceleration(dev, verbose=False):
    global pl_puf

    o = pl_puf[dev.orientation]
    x, y, z = dev.acceleration
    if verbose:
        print(f"\rOrientation: {o}, Acceleration: X:{x:.2f}, Y: {y:.2f}, Z: {z:.2f} m/s^2", end="\r")
    return x, y, z

if __name__ == "__main__":
    dev = init_device()
    while True:
        track_acceleration(dev, verbose=True)
        time.sleep(0.1)
