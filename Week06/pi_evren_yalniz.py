import random

def next_pi(n):
    points_in_circle = 0
    points_in_total = 0

    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)

        dist = x**2 + y**2

        if dist <= 1 :
            points_in_circle += 1
        points_in_total += 1

        yield 4 * points_in_circle / points_in_total
