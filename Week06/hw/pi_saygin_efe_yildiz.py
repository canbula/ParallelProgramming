import random

def next_pi():
    num_in = 1
    num_out = 1

    while True:
        x = random.random()
        y = random.random()

        if x**2+y**2 <= 1:
            num_in += 1
        else:
            num_out += 1
        yield 4*(num_in/(num_in+num_out))

if __name__ == "__main__":
    np = next_pi()
    for _ in range(1_000_000):
        next(np)
    print(next(np))

