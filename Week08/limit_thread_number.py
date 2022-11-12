import threading
import time
import random


class LimitThreads(threading.Thread):
    def __init__(self, n: int = 1):
        super().__init__()
        self.n = n  # Add 2 for the main thread and the thread that runs this class
        self.daemon = True
        self.name = "LimitThreads"

    def run(self):
        while True:
            time.sleep(0.1)
            print(f"{threading.active_count()}/{self.n} Threads:", end=" ")
            i = 0
            for t in threading.enumerate():
                print(f"{i}: {t.name}", end=" ")
                i += 1
                if i > self.n:
                    t.join()
            print()


class Thread2Create(threading.Thread):
    def __init__(self):
        super().__init__()
        self.go = True

    def run(self):
        n = random.randint(5, 10)
        for i in range(n):
            if not self.go:
                print(f"Thread {self.name} stopped")
                return
            print(f"Thread {self.name} will live for {n-i}/{n} seconds")
            time.sleep(1)

    def join(self, timeout=None):
        self.go = False


def main():
    thread_limiter = LimitThreads(5)
    thread_limiter.start()
    while True:
        time.sleep(1)
        Thread2Create().start()


if __name__ == '__main__':
    main()
