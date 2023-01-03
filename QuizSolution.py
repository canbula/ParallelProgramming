import os
from multiprocessing import Process, Array
import time
import random

class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1

class FindEuler:
    def __init__(self):
        self.count = 0
        self.b = 0
        self.x = 0
    def monte_carlo_estimate(self, number_of_samples, shared_p ,p):
        samples = []
        for i in range(number_of_samples):
            n = 0
            s = 0
            while(s <= 1):
                random_number = random.uniform(0, 1)
                s += random_number
                n += 1
            samples.append(n)

        total = 0
        for c in samples:
            total += c
        shared_p[p] = total / len(samples)


if __name__ == '__main__':
    for number_of_p in range(1, os.cpu_count() + 1):
        num_samples = 100000
        tt = TicToc()
        tt.tic()
        find_eulers = []
        processes = []
        shared_e = Array('f', [0]*number_of_p)
        for i in range(number_of_p):
            find_eulers.append(FindEuler())
            processes.append(Process(target=find_eulers[i].monte_carlo_estimate, args=(num_samples, shared_e, i)))

        for process in processes:
            process.start()

        for process in processes:
            process.join()

    total = 0
    for n in shared_e:
        total += n
    e = total / len(find_eulers)

    print(f"Number Of Process = {number_of_p} | Estimated Euler Number = {e:.8f} | Time = {tt.toc():.8f} seconds")
