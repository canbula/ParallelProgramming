import random
import numpy as np

def next_pi():
    inner = 0
    total = 0

    while True:
        x = np.random.rand()
        y = np.random.rand()
        total += 1

        if x ** 2 + y ** 2 <= 1:
            inner += 1

        yield 4 * (inner / total)

if __name__ == "__main__":
    pi_estimate = next_pi()

    for i in range(20000):
        pi_estimated = next(pi_estimate)

    print(pi_estimated)
