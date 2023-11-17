import random


def next_pi():
    circle_area_points = 0
    square_area_points = 0

    while True:
        random_x = random.random()
        random_y = random.random()

        if random_x**2 + random_y**2 <= 1:
            circle_area_points += 1
        square_area_points += 1

        pi = 4 * circle_area_points / square_area_points
        yield pi
