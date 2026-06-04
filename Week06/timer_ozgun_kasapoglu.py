import time

class Timer:
    def __init__(self):
        self.start_time = 0.0
        self.end_time = 0.0

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, a, b, c):
        self.end_time = time.time()
