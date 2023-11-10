import random

def next_pi():
    inner_points = 0
    total_points = 0

    while True:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x**2 + y**2) < 1:
            inner_points += 1
        total_points += 1

        pi = 4 * (inner_points / total_points)
        yield pi


