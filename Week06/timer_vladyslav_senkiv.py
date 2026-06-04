from time import perf_counter


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = perf_counter()
        return False
