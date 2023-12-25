import random

def next_pi():
    in_circle = 0
    all_area = 0

    while True:
        x = random.random()
        y = random.random()
        all_area += 1

        if x**2 + y**2 <= 1:
            in_circle += 1

        predicted_pi = 4 * in_circle / all_area
        yield predicted_pi
