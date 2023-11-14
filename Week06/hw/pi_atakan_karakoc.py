import random

# class Pi:
#     def __init__(self):
#         self.outer = 0
#         self.inner = 0

#     def get_outer(self):
#         return self.outer

#     def get_inner(self):
#         return self.inner

def next_pi():
    inner, outer = 0, 0
    while True:
        rand_x, rand_y = random.random(), random.random()
        if rand_x ** 2 + rand_y ** 2 <= 1:
            inner += 1
        outer += 1
        pi = 4 * (inner / outer)
        yield pi


if __name__ == '__main__':
    pi_generator = next_pi()

    for i in range(10000):
        print(f"{next(pi_generator)}")

