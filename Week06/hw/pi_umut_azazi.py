import random

def next_pi():
    inside_circle = 0
    total_points = 0
    while True:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        total_points += 1
        if x**2 + y**2 <= 1:
            inside_circle += 1
        yield 4 * inside_circle / total_points
