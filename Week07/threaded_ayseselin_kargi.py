import threading
import random
import math


def threaded(n):
    """
    A decorator that creates n threads from a function.
    Each call to the decorated function spawns n threads,
    all running the original function with the same arguments,
    and waits for all of them to finish before returning.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []
            for _ in range(n):
                t = threading.Thread(target=func, args=args, kwargs=kwargs)
                threads.append(t)
            for t in threads:
                t.start()
            for t in threads:
                t.join()
        return wrapper
    return decorator

if __name__ == "__main__":
    results = []
    lock = threading.Lock()

    @threaded(4)
    def estimate_pi(num_samples):
        inside = 0
        for _ in range(num_samples):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if math.sqrt(x**2 + y**2) <= 1:
                inside += 1
        with lock:
            results.append(inside / num_samples * 4)

    estimate_pi(100000)

    pi_estimate = sum(results) / len(results)
    print(f"Estimated Pi: {pi_estimate:.6f}")
    print(f"Actual Pi:    {math.pi:.6f}")
    print(f"Error:        {abs(pi_estimate - math.pi):.6f}")
