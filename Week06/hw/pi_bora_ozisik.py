import random

def next_pi():
    outer = 0
    inner = 0
    while True:
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inner += 1
        outer += 1
        pi = 4 * (inner / outer)
        yield pi
