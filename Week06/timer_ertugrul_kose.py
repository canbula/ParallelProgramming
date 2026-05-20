import time

class ExecutionTimer:
    
    def __init__(self):
        self.start_timestamp = None
        self.finish_timestamp = None

    def __enter__(self):
        self.start_timestamp = time.time()
        return self  

    def __exit__(self, exc_type, exc_value, traceback):
        self.finish_timestamp = time.time()
