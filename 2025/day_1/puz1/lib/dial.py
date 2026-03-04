import sys

class Dial:
    def __init__(self, tick=50):
        self.tick = tick


    def __repr__(self):
        return str(self.tick)


    def turn(self, cmd):
        match cmd[0]:
            case 'R':
                self.right(int(cmd[1:]))
            case 'L':
                self.left(int(cmd[1:]))
            case _:
                sys.exit(f"Invalid Motion: {cmd}")

        return str(self.tick)


    def right(self, clicks):
        self.tick = ( self.tick + clicks ) % 100


    def left(self, clicks):
        self.tick = ( self.tick - clicks + 100 ) % 100
