import numpy as np


def next_pi() -> np.float64:
    total = 0
    inner = 0
    while True:
        x = np.random.rand()
        y = np.random.rand()
        if (x**2 + y**2) <= 1:
            inner += 1
        total += 1
        yield np.float64(((inner / total) * 4))


def main():
    real_pi = np.pi
    i = 0
    desired_accuracy = np.float64(1.0e-12)
    np.random.seed(7)
    for pi in next_pi():
        i += 1
        accuracy = np.abs(pi - real_pi)
        print(
            f"Iteration: {i:10d} | Estimated Pi: {pi:10.8f} | Real Pi: {real_pi:10.8f} | Accuracy: {accuracy:10.8f}"
        )
        if accuracy < desired_accuracy:
            break


if __name__ == "__main__":
    main()
