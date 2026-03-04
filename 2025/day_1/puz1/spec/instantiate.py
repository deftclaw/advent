from   lib.dial import dial
import time

dial    = lambda d: Dial(0)
string  = lambda d: str(d)
integer = lambda d: int(str(d))

def time_trial(func):
    dl    = Dial(0)
    start = time.time()

    for i in range(1000):
        func(dl)

    end = time.time()

    print(f"elapsed: {end - start}")


for f in [dial, string, integer]:
    time_trial(f)

# >>> elapsed: 0.00010776519775390625
# >>> elapsed: 0.00013637542724609375
# >>> elapsed: 0.00018548965454101562
