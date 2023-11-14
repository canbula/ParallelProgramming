import random

def next_pi():
    inner = 0
    total = 0
    while True:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x**2 + y**2) <= 1:
            inner += 1
        total += 1
        pi = 4 * (inner / total)
        yield pi
