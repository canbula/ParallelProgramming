import threading


class IncreaseCounter(threading.Thread):
    def __init__(self, counter, n):
        super().__init__()
        self.counter = counter
        self.n = n

    def run(self):
        for _ in range(self.n):
            self.counter.increase()


class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1


class LockedCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increase(self):
        with self.lock:
            self.count += 1


def main(n: int, m: int, locked: bool = False):
    counter = Counter() if not locked else LockedCounter()
    threads = []
    for _ in range(m):
        t = IncreaseCounter(counter, n)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Expected: {n*m}, Actual: {counter.count}")
    return counter.count


if __name__ == "__main__":
    number_of_threads = 4
    for size in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        try:
            assert main(size, number_of_threads, True) == size * number_of_threads
        except AssertionError:
            print(f"Failed for size {size}")
        else:
            print(f"Success for size {size}")
