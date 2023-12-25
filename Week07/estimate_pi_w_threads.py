import random
import threading
import numpy as np
from pprint import pprint


results = []


def next_pi() -> float:
    total = 0
    inner = 0
    while True:
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <= 1:
            inner += 1
        total += 1
        yield float(((inner / total) * 4))


def pi_until_accuracy(desired_accuracy: float) -> float:
    real_pi = np.pi
    i = 0
    for pi in next_pi():
        i += 1
        accuracy = np.abs(pi - real_pi)
        print(
            f"Iteration: {i:10d} | Estimated Pi: {pi:10.8f} | Real Pi: {real_pi:10.8f} | Accuracy: {accuracy:10.8f}"
        )
        if accuracy < desired_accuracy:
            break
    results.append(
        {
            "pi": pi,
            "i": i,
            "accuracy": accuracy,
            "thread_id": threading.get_native_id(),
        }
    )
    return pi, i, accuracy


def main():
    # create a thread to estimate pi
    # create a thread to print the current estimate
    # join the threads
    # print the final estimate
    thread = threading.Thread(target=pi_until_accuracy, args=(1.0e-6,))
    thread.start()
    thread.join()
    pprint(results)


def main_threads():
    accuracies = [1.0e-10, 1.0e-10, 1.0e-10, 1.0e-10]
    threads = []
    for accuracy in accuracies:
        thread = threading.Thread(target=pi_until_accuracy, args=(accuracy,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    pprint(results)


if __name__ == "__main__":
    main_threads()
