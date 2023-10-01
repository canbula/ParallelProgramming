import multiprocessing
import random
import math


class MonteCarloPi(multiprocessing.Process):
    def __init__(self, n, q, seed=None):
        super().__init__()
        self.n = n
        self.q = q
        self.seed = seed

    def run(self):
        if self.seed is not None:
            random.seed(self.seed)
        count = 0
        for i in range(self.n):
            x = random.random()
            y = random.random()
            if math.sqrt(x**2 + y**2) < 1:
                count += 1
        self.q.put(count)


def mcpi(m, n):
    q = multiprocessing.Queue()
    processes = [MonteCarloPi(n, q) for _ in range(m)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return 4 * sum(q.get() for _ in processes) / (m * n)


if __name__ == '__main__':
    print(mcpi(multiprocessing.cpu_count(), 10000000))
