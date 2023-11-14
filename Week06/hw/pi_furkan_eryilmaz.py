import random
import math

def next_pi():    
    points_inside = 0
    points_outside = 0
    
    while True:
        x = random.random()
        y = random.random()

        if math.sqrt(x**2 + y**2) < 1:
            points_inside += 1
        else:
            points_outside += 1

        _estimated_pi = 4 * points_inside / (points_inside + points_outside)
        yield _estimated_pi

if __name__ == "__main__":
    estimated_pi = next_pi()

    while True:
        print(next(estimated_pi))