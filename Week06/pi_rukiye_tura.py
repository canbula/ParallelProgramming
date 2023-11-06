import random

def generator(total):
    points_in_circle = 0

    for i in range(total):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            points_in_circle += 1

        yield 4 * points_in_circle / (i + 1)
