import random

class Pi:
    def __init__(self):
        self.outer = 0
        self.inner = 0

    def get_outer(self):
        return self.outer

    def get_inner(self):
        return self.inner

    def next_pi(self):
        while True:
            rand_x, rand_y = random.random(), random.random()
            if rand_x ** 2 + rand_y ** 2 <= 1:
                self.inner += 1
            self.outer += 1
            pi = 4 * (self.inner / self.outer)
            yield pi


if __name__ == '__main__':
    p = Pi()
    pi_generator = p.next_pi()

    for i in range(10000):
        print(next(pi_generator))
        # print(f"Outer:{p.get_outer()} - Inner: {p.get_inner()} - pi: {next(pi_generator)}")

    print(f"Total Outer: {p.get_outer()} ----- Total Inner: {p.get_inner()}")

