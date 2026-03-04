from lib.color      import clr, gold
from lib.dial       import Dial
from lib.read_array import read_lines

def main():
    dial         = Dial()
    instructions = read_lines('../input.txt')
    zeros        = 0


    for cmd in instructions:
        print(f"{cmd}: {dial.turn(cmd)}", end="")
        
        if dial.tick == Dial(0).tick:
            zeros += 1
            print(f" {gold}{zeros}{clr}")
        else:
            print()

    print(f"Solution: {gold}{zeros}{clr}")


main()
