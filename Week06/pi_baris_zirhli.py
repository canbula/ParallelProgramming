import random

def next_pi() -> None:
    inner, outter = 0, 0
    while True:
        randomX, randomY = random.random(), random.random()
        if randomX**2 + randomY**2 <= 1:
            inner += 1
        outter += 1

        pi = 4 * (inner / outter)
        yield pi


if __name__ == "__main__":
    pi = next_pi()

    for i in range(10000000):
        print(f"{next(pi)}")
