import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self  # with ... as t → t'yi döndürmek için

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
