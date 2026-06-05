import time


class Timer:
    """
    A context manager class that measures the time taken
    by the block of code it manages.
    """

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        print(f"Elapsed time: {self.end_time - self.start_time:.6f} seconds")
        return False
