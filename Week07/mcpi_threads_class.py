import random
import threading


class DartThrower(threading.Thread):
    def __init__(self, num_darts, index):
        super().__init__()
        self.num_darts = num_darts
        self.index = index
        self.num_hits = 0

    def run(self):
        for i in range(self.num_darts):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x*x + y*y <= 1:
                self.num_hits += 1
        print(f"Thread {self.index} finished and got {self.num_hits} hits: {self.num_hits/self.num_darts*4}")


def main():
    num_darts = 100000000
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
