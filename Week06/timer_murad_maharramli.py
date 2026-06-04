import time

class Timer:
    """
    A context manager class that measures the execution time of a code block.
    """
    def __init__(self):
        # Initialize the required public attributes
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        # time.perf_counter() is used instead of time.time() for the highest 
        # available resolution when measuring short durations.
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Record the end time the moment the code block finishes
        self.end_time = time.perf_counter()
        
        # Returning False ensures that if an exception occurs inside the 'with' block, 
        # it is not suppressed and raises normally.
        return False
