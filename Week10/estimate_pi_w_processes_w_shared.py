import multiprocessing
import random
import numpy as np
import os


def generate_points(n, inner, total, lock):
    local_inner = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <= 1:
            local_inner += 1
    with lock:
        inner.value += local_inner
        total.value += n


def pi(accuracy: float = 1.0e-5, number_of_processes: int = 1) -> float:
    def pi_(inner_: int, total_: int) -> float:
        try:
            return (inner_ / total_) * 4
        except ZeroDivisionError:
            return 0.0

    BATCH_SIZE = 1000000
    total = multiprocessing.Value("i", 0, lock=False)
    inner = multiprocessing.Value("i", 0, lock=False)
    process_count = 0
    lock = multiprocessing.Lock()
    while abs(pi_(inner.value, total.value) - np.pi) > accuracy:
        processes = []
        for _ in range(number_of_processes):
            p = multiprocessing.Process(
                target=generate_points, args=(BATCH_SIZE, inner, total, lock)
            )
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        process_count += len(processes)
        print(
            f"inner: {inner.value}, total: {total.value}, process_count: {process_count}, pi: {pi_(inner.value, total.value)}"
        )
    return pi_(inner.value, total.value)


if __name__ == "__main__":
    multiprocessing.set_start_method("fork")
    print(pi(number_of_processes=os.cpu_count()))
