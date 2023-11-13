import random

def next_pi():
    inner = 0
    total = 0

    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        total += 1

        distance = x ** 2 + y ** 2

        if distance <= 1:
            inner += 1

        estimated_pi = (inner / total) * 4
        yield estimated_pi, total




