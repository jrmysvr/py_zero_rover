import sys
from gpiozero import Servo 

class Rover:
    class _Rover:
        def __init__(self):
            self.right = Servo(12)
            self.right.detach()
            self.left = Servo(13)
            self.left.detach()

    _rover = None

    def __init__(self):
        if Rover._rover is None:
            Rover._rover = self._Rover()
    
    def forward(self):
        self._rover.left.max()
        self._rover.right.min()

    def turn_left(self):
        self._rover.left.detach()
        self._rover.right.min()

    def turn_right(self):
        self._rover.right.detach()
        self._rover.left.max()

    def stop(self):
        self._rover.left.detach()
        self._rover.right.detach()

if __name__ == "__main__":
    if "--demo" in sys.argv:
        import time
        rover = Rover()
        def demo(rover: Rover):
            rover.forward()
            time.sleep(1)
            rover.turn_left()
            time.sleep(1)
            rover.forward()
            time.sleep(2)
            rover.turn_right()
            time.sleep(1)
            rover.forward()
            time.sleep(1)
            rover.stop()

        demo(rover)

    else:
        from keyboard import Listener
        print("======================")
        print("Initializing Rover")
        rover = Rover()
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
        listener.listen(cb=control_rover)

        print("Exiting...")
        sys.exit(0)

