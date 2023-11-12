import random
import numpy as np


def next_pi():
    num_inside = 0
    num_total = 0

    while True:
        x = np.random.rand()
        y = np.random.rand()
        num_total += 1

        if x ** 2 + y ** 2 <= 1:
            num_inside += 1

        yield 4 * (num_inside / num_total)


if __name__ == "__main__":
    estimate_pi = next_pi()

    for i in range(10000):
        estimated_pi = next(estimate_pi)

    print(estimated_pi)
