import os
import pytest
import time

class Timer:
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")

    def __enter__(self) -> "Timer":
        print(f"Entering {self.__class__.__name__}")
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print(f"Exiting {self.__class__.__name__}")
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        return True