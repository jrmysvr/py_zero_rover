import sys
from i2c import imu_mma
from gpio.keyboard import Listener
from gpio.rover import Rover
import threading
import time

RUNNING = False

def control_rover(key):
    global rover 
    if key == 'UP':
        rover.forward()
    elif key == 'RIGHT':
        rover.turn_right()
    elif key == 'DOWN':
        rover.stop()
    elif key == 'LEFT':
        rover.turn_left()

def track_acceleration(dev, verbose):
    global RUNNING 
    while RUNNING:
        imu_mma.track_acceleration(dev, verbose)
        time.sleep(0.25)

if __name__ == "__main__":
    RUNNING = True
    print("Starting")

    dev = imu_mma.init_device()
    mma_thread = threading.Thread(target=track_acceleration, args=[dev, True])
    print("======================")
    print("Initializing Rover")
    rover = Rover()
    print("----------------------")
    print("Initializing Listener")
    listener = Listener()
    print("Listening for input...")
    print("----------------------")
    print("Up Arrow     : Go Forward")
    print("Right Arrow  : Go Right")
    print("Left Arrow   : Go Left")
    print("Down Arrow   : Stop")
    print("Press Ctrl+D to exit")
    print("----------------------")
    mma_thread.start()
    listener.listen(cb=control_rover)

    RUNNING = False
    print("Exiting...")
    sys.exit(0)

