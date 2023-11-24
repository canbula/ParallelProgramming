import random

def next_pi():
    points_in = 0
    total_points = 0

    while True:
        x = random.uniform(0,1)
        y = random.uniform(0,1)

        dist = x**2 + y**2

        if dist <= 1 :
            points_in += 1
        total_points += 1

        pi_val = 4 * points_in / total_points
        yield pi_val
