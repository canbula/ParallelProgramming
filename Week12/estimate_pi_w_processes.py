import multiprocessing
import random
import numpy as np
import os


def generate_points(n):
    inner = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <= 1:
            inner += 1
    return inner


def pi(accuracy: float = 1.0e-5, number_of_processes: int = 1) -> float:
    def pi_(inner_: int, total_: int) -> float:
        try:
            return (inner_ / total_) * 4
        except ZeroDivisionError:
            return 0.0

    BATCH_SIZE = 1000000
    total = 0
    inner = 0
    process_count = 0
    while abs(pi_(inner, total) - np.pi) > accuracy:
        with multiprocessing.Pool(processes=number_of_processes) as pool:
            results = pool.map(
                generate_points, [BATCH_SIZE for _ in range(number_of_processes)]
            )
            inner += sum(results)
            total += len(results) * BATCH_SIZE
            process_count += len(results)
        print(
            f"inner: {inner}, total: {total}, process_count: {process_count}, pi: {pi_(inner, total)}"
        )
    return pi_(inner, total)


if __name__ == "__main__":
    multiprocessing.set_start_method("fork")
    print(pi(number_of_processes=os.cpu_count()))
