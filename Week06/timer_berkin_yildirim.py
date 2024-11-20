import time
from typing import Optional, Callable

class Timer:
    def __init__(self, log: bool = True, callback: Optional[Callable[[float], None]] = None):
        """
        Initialize the Timer with optional logging and a callback function.
        :param log: If True, logs start and end messages; if False, remains silent.
        :param callback: An optional function to call with the elapsed time when exiting.
        """
        self.log = log
        self.callback = callback
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        if self.log:
            print(f"{self.__class__.__name__} initialized.")

    def __enter__(self) -> "Timer":
        """
        Start the timer upon entering the context.
        """
        self.start_time = time.time()
        if self.log:
            print(f"{self.__class__.__name__} started.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Stop the timer upon exiting the context and calculate the elapsed time.
        Calls the callback function if provided.
        """
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        if self.log:
            print(f"{self.__class__.__name__} ended. Elapsed time: {self.elapsed_time:.4f} seconds")
        
        # If a callback is provided, call it with the elapsed time
        if self.callback:
            self.callback(self.elapsed_time)
        
        # Return False to allow any exceptions to propagate
        return False
