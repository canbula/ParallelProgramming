import time

class Timer():

    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.used_time = self.end_time - self.start_time
        print(f"used time,{self.used_time:.5f},seconds")
