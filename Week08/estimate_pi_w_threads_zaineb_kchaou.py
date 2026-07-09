import random
import threading
import math

class PiCalculator(threading.Thread):
    def __init__(self, samples):
        super().__init__()
        self.samples = samples
        self.count_inside = 0

    def run(self):
        for _ in range(self.samples):
            px = random.uniform(0, 1)
            py = random.uniform(0, 1)

            if (px ** 2 + py ** 2) <= 1:
                self.count_inside += 1

def calculate_pi(total_samples=1000000, num_threads=4):
    workers = []
    samples_per_worker = total_samples // num_threads
    for i in range(num_threads):
        worker = PiCalculator(samples_per_worker)
        workers.append(worker)
        worker.start()
    total_inside = sum(
        worker.count_inside
        for worker in workers
        if not worker.join()
    )

    return 4 * total_inside / (samples_per_worker * num_threads)

if __name__ == "__main__":
    estimated_pi = calculate_pi(1000000, 4)

    print(f"Estimated value of PI: {estimated_pi}")
    print(f"Actual value of PI: {math.pi}")
    print(f"diff : {abs(estimated_pi - math.pi)}")
