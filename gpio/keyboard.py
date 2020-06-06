from .getch import _GetchUnix

class Listener:
    def __init__(self):
        self.getch = _GetchUnix()
    
    def listen(self, cb=None, verbose=False):
        while True:
            key = self.getch()
            if key == '\x04': # Ctrl + D
                if verbose:
                    print("Entered: ", repr(key))
                break

            if key == '\x1b':
                ch0 = self.getch()
                ch1 = self.getch()
                if ch1 == 'A':
                    key = 'UP' 
                elif ch1 == 'C':
                    key = 'RIGHT'
                elif ch1 == 'B':
                    key = 'DOWN'
                elif ch1 == 'D':
                    key = 'LEFT'
                else:
                    key = key + ch0 + ch1
    
            if verbose:
                print("Entered: ", repr(key))

            if cb:
                cb(key)
