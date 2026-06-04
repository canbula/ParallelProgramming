import threading
import random
import numpy as np
from numba import jit


class PiEstimatorThread(threading.Thread):
    def __init__(
        self,
        number_of_points: int = 100000,
        name="Generator",
    ):
        super().__init__(name=name)
        self.number_of_points = number_of_points
        self.inner_points = 0
        self.total_points = 0

    @staticmethod
    @jit(nopython=True, nogil=True)
    def generate_points(n):
        inner_points = 0
        total_points = 0
        for _ in range(n):
            x = random.random()
            y = random.random()
            if x**2 + y**2 <= 1:
                inner_points += 1
            total_points += 1
        return inner_points, total_points

    def run(self):
        self.inner_points, self.total_points = self.generate_points(
            self.number_of_points
        )


class PiEstimator(threading.Thread):
    def __init__(
        self,
        desired_accuracy: float = 1.0e-4,
        number_of_threads: int = 4,
        chunk_size: int = 100000,
        name="PI Estimator",
    ):
        super().__init__(name=name)
        self.desired_accuracy = desired_accuracy
        self.number_of_threads = number_of_threads
        self.chunk_size = chunk_size
        self.inner_points = 0
        self.total_points = 0
        self.generated_threads = 0

    def pi(self):
        try:
            return 4 * self.inner_points / self.total_points
        except ZeroDivisionError:
            return 0.0

    def accuracy(self):
        return abs(np.pi - self.pi())

    def run(self):
        while self.accuracy() > self.desired_accuracy:
            threads = []
            for _ in range(self.number_of_threads):
                threads.append(
                    PiEstimatorThread(
                        number_of_points=self.chunk_size,
                        name=f"Generator - {self.generated_threads}",
                    )
                )
                self.generated_threads += 1
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            for thread in threads:
                self.inner_points += thread.inner_points
                self.total_points += thread.total_points

    def join(self, timeout=None):
        super().join()
        print(f"Final estimation of Pi: {self.pi()}")
        print(f"Accuracy: {self.accuracy()}")
        print(f"Number of total points: {self.total_points}")
        print(f"Number of inner points: {self.inner_points}")
        print(f"Number of threads: {self.generated_threads}")


if __name__ == "__main__":
    pi_estimator = PiEstimator(
        desired_accuracy=1.0e-8,
        number_of_threads=16,
        chunk_size=10000000,
        name="Pi Estimator",
    )
    pi_estimator.start()
    pi_estimator.join()
