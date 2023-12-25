import random
import math

def next_pi():    
    total_points = 0
    inner_points = 0
    
    while True:
        x = random.random()
        y = random.random()
        z = math.sqrt(x**2 + y**2)
        total_points += 1
        if z <= 1:
            inner_points += 1
        pi_estimate = 4 * inner_points / total_points
        yield pi_estimate
