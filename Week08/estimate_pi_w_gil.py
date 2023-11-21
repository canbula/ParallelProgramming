import threading
import random
import numpy as np
import string


class PiEstimatorThread(threading.Thread):
    def __init__(self, number_of_points: int = 10000, name: str = None) -> None:
        super().__init__()
        self.number_of_points: int = number_of_points
        self.name: str = name or "".join(random.choices(string.ascii_letters, k=8))
        self.inner: int = 0

    def generate_points(self):
        for _ in range(self.number_of_points):
            x = random.random()
            y = random.random()
            if (x**2 + y**2) <= 1:
                self.inner += 1

    def run(self) -> None:
        self.generate_points()


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


def main() -> None:
    desired_accuracy = 1.0e-10
    number_of_threads = 8
    chunk_size = 1000000
    pi_estimator = PiEstimator(
        accuracy=desired_accuracy,
        number_of_threads=number_of_threads,
        chunk_size=chunk_size,
    )
    pi_estimator.start()
    pi_estimator.join()


if __name__ == "__main__":
    main()
