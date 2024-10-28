import time

class Timer:
    def __init__(self) -> None: 
        self.start_time = None
        self.end_time = None

    def __enter__(self) -> "Timer":
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Task finished! It took {elapsed_time:.2f} seconds.")
        return False
