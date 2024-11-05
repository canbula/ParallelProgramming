import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.duration= None
    
    def __enter__(self):
        self.start_time = time.time()  
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time() 
        self.duration = self.end_time - self.start_time
        print(f"Duration is : {self.duration} seconds.")
