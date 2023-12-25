import threading
import random
import numpy as np
import string
from numba import jit
from memory_profiler import memory_usage
import time


class PiEstimatorThread(threading.Thread):
    def __init__(self, number_of_points: int = 10000, name: str = None) -> None:
        super().__init__()
        self.number_of_points: int = number_of_points
        self.name: str = name or "".join(random.choices(string.ascii_letters, k=8))
        self.inner: int = 0

    @staticmethod
    @jit(nopython=True, nogil=True)
    def generate_points(n):
        inner = 0
        for _ in range(n):
            x = random.random()
            y = random.random()
            if (x**2 + y**2) <= 1:
                inner += 1
        return inner

    def run(self) -> None:
        self.inner = self.generate_points(self.number_of_points)


class PiEstimator(threading.Thread):
    def __init__(
        self,
        accuracy: float = 1.0e-5,
        number_of_threads: int = 1,
        chunk_size: int = 10000,
        name: str = "PiEstimator",
    ) -> None:
        super().__init__()
        self.desired_accuracy: float = accuracy
        self.number_of_threads: int = number_of_threads
        self.chunk_size: int = chunk_size
        self.name: str = name
        self.total: int = 0
        self.inner: int = 0
        self.threads = []
        self.generated_threads: int = 0

    def pi(self) -> float:
        try:
            return float((self.inner / self.total) * 4)
        except ZeroDivisionError:
            return 0.0

    def accuracy(self) -> float:
        return abs(self.pi() - np.pi)

    def run(self):
        while self.accuracy() > self.desired_accuracy:
            for _ in range(self.number_of_threads):
                thread = PiEstimatorThread(
                    self.chunk_size,
                    name=f"Generator-{self.generated_threads}",
                )
                self.generated_threads += 1
                thread.start()
                self.threads.append(thread)
            for thread in self.threads:
                thread.join()
                self.inner += thread.inner
                self.total += thread.number_of_points
            self.threads = []

    def join(self):
        super().join()
        print(f"Final Estimate of Pi: {self.pi()}")
        print(f"Accuracy: {self.accuracy()}")
        print(f"Total Number of Points Inside the Circle: {self.inner}")
        print(f"Total Number of Points Generated: {self.total}")
        print(f"Total Number of Generated Threads: {self.generated_threads}")


class PiMonitor(threading.Thread):
    def __init__(self) -> None:
        super().__init__()
        self.daemon = True
        self.name = "Monitor"

    def run(self) -> None:
        while True:
            print(f"Running threads: {threading.active_count()} | ", end="")
            threads = threading.enumerate()
            for thread in threads:
                print(f"{thread.name} ", end="")
            print()
            for thread in threads:
                if thread.name == "PiEstimator":
                    print(
                        f"Pi = {thread.pi():10.8f} | Accuracy = {thread.accuracy():.2e} | Total = {thread.total:10d} | Threads = {thread.generated_threads:10d}"
                    )
            time.sleep(1)


def performance(func):
    def _performance(*args, **kwargs):
        start = time.perf_counter()
        memory = memory_usage((func, args, kwargs))
        end = time.perf_counter()
        print(f"Time taken: {end - start:.2f}s")
        print(f"Memory used: {max(memory) - min(memory):.2f}MiB")

    return _performance


@performance
def main() -> None:
    monitor = PiMonitor()
    monitor.start()
    desired_accuracy = 1.0e-8
    number_of_threads = 8
    chunk_size = 1000000000
    pi_estimator = PiEstimator(
        accuracy=desired_accuracy,
        number_of_threads=number_of_threads,
        chunk_size=chunk_size,
    )
    pi_estimator.start()
    pi_estimator.join()


if __name__ == "__main__":
    main()
