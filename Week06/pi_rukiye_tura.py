import random

def next_pi():
    points_in_circle = 0
    points_out_circle = 0 
    while True: 
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            points_in_circle += 1
        points_out_circle += 1 
        yield 4 * points_in_circle / points_out_circle 
