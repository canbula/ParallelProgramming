import threading


class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increase(self):
        with self.lock:
            self.count += 1


class IncreaseCounter(threading.Thread):
    def __init__(self, counter, n):
        super().__init__()
        self.counter = counter
        self.n = n

    def run(self):
        for _ in range(self.n):
            self.counter.increase()


def main(n: int, m: int):
    counter = Counter()
    threads = []
    for _ in range(m):
        t = IncreaseCounter(counter, n)
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Expected: {n*m}, Actual: {counter.count}")
    return counter.count


if __name__ == "__main__":
    main(1000000, 4)
