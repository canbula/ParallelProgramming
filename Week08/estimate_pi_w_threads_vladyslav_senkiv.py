import random
import threading
import math


class PiWorker(threading.Thread):
    def __init__(self, points_count):
        super().__init__()
        self.points_count = points_count
        self.inside_circle = 0

    def run(self):
        for _ in range(self.points_count):
            x = random.random()
            y = random.random()

            if x * x + y * y <= 1:
                self.inside_circle += 1


def estimate_pi(total_points=1000000, thread_count=4):
    points_per_thread = total_points // thread_count
    threads = []

    for _ in range(thread_count):
        thread = PiWorker(points_per_thread)
        threads.append(thread)
        thread.start()

    inside_circle = 0

    for thread in threads:
        thread.join()
        inside_circle += thread.inside_circle

    used_points = points_per_thread * thread_count
    pi_value = 4 * inside_circle / used_points

    return pi_value


if __name__ == "__main__":
    pi = estimate_pi(total_points=1000000, thread_count=4)

    print("Estimated PI:", pi)
    print("Real PI:", math.pi)
    print("Difference:", abs(math.pi - pi))
