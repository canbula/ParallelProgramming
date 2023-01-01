import multiprocessing
import random


class EstimateEuler(multiprocessing.Process):
    def __init__(self, q: multiprocessing.Queue, n: int, seed: int = None):
        super().__init__()
        self.q = q
        self.n = n
        self.seed = seed

    def run(self):
        if self.seed is not None:
            random.seed(self.seed)
        count_to_queue = 0
        for _ in range(self.n):
            count = 0
            s = 0
            while s < 1:
                s += random.random()
                count += 1
            count_to_queue += count
        self.q.put(count_to_queue)


def estimate_euler(m: int, n: int):
    q = multiprocessing.Queue()
    processes = [EstimateEuler(q, n) for _ in range(m)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return sum(q.get() for _ in processes) / (m * n)


if __name__ == '__main__':
    print(estimate_euler(8, 10000000))
