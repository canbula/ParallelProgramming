from time import time as tm

class Timer:

    def __enter__(self): 
        self.start_time = tm()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = tm()