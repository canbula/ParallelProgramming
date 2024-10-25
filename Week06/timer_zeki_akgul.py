import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
      
    def __enter__(self):
        self.start_time = time.time()
        return self 
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Managed code block took {self.elapsed_time} seconds")
