import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()  # Record the start time
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()  # Record the end time
