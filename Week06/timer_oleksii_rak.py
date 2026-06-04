from time import perf_counter

class Timer:
    def __init__(self):
        self.start_time = 0.0
        self.end_time = 0.0

    def __enter__(self):
        self.start_time = perf_counter()
        return self
      
    def __exit__(self, *args):
        self.end_time = perf_counter()
