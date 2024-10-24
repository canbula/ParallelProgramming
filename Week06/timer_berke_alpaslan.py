import time

class Timer:
    """
        A context manager that measures the elapsed time of a code block.

        This class allows you to measure the time taken to execute
        a block of code using the context management protocol.
        It records the start time when entering the context and
        the end time when exiting the context, allowing you to
        calculate and print the elapsed time.

        Attributes:
            start_time (float): The time when the timer starts.
            end_time (float): The time when the timer ends.

        Example:
            >>> with Timer() as timer:
            ...     time.sleep(2)
            ...
            Elapsed time: 2.0000 seconds
    """
    def __init__(self):
        """
           Initializes the Timer with start and end times set to None.

            Attributes:
            start_time (float): The time when the timer starts (initially None).
            end_time (float): The time when the timer ends (initially None).
        """
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        """
            Starts the timer by recording the current time.

           Returns:
           Timer: The Timer instance, allowing access to start and end times.
        """
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
            Stops the timer and calculates the elapsed time.

            This method is called when exiting the context. It calculates
            the elapsed time and prints it.

            Args:
                exc_type: The exception type (if an exception occurred).
                exc_value: The exception value (if an exception occurred).
                traceback: The traceback object (if an exception occurred).

            Returns:
                bool: Returns False to propagate any exceptions that occurred.
         """
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"\n\nElapsed time: {elapsed_time:.4f} seconds")
        return False
