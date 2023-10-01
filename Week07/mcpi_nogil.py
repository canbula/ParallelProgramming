import random
import threading
from numba import jit
import time


def see_threads():
    while True:
        # print(threading.enumerate())
        for t in threading.enumerate():
            print(t.name, end=' ')
        print()
        time.sleep(1)


class DartThrower(threading.Thread):
    def __init__(self, num_darts, index):
        super().__init__()
        self.num_darts = num_darts
        self.index = index
        self.num_hits = 0

    def run(self):
        self.num_hits = self.throw_darts(self.num_darts)
        print(f"Thread {self.index} finished and got {self.num_hits} hits: {self.num_hits/self.num_darts*4}")

    @staticmethod
    @jit(nopython=True, nogil=True)
    def throw_darts(num_darts):
        num_hits = 0
        for i in range(num_darts):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x*x + y*y <= 1:
                num_hits += 1
        return num_hits


def main():
    t = threading.Thread(target=see_threads, daemon=True)
    t.start()
    num_darts = 10000000000
    num_threads = 16
    num_darts_per_thread = num_darts // num_threads
    threads = []
    for i in range(num_threads):
        t = DartThrower(num_darts_per_thread, i)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    num_hits = sum(t.num_hits for t in threads)
    print(f"Main thread finished and got {num_hits} hits: {num_hits/num_darts*4}")


if __name__ == '__main__':
    main()
