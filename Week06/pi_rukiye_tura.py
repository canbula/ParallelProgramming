import random

def next_pi():
    points_in_circle = 0
    total_points = 0 
    while True: 
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            points_in_circle += 1
        total_points += 1 
        yield 4 * points_in_circle / total_points
