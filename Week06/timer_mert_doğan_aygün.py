import time

class ExecutionTimer:
    """
    A context manager to measure and display the elapsed time for a block of code.

    The ExecutionTimer calculates the time spent inside a context block, 
    recording the start and end times to determine the elapsed duration.

    Attributes:
        start_time (float): Records when the timer starts.
        end_time (float): Records when the timer stops.

    Example:
        >>> with ExecutionTimer() as timer:
        ...     time.sleep(2)
        ...
        Elapsed time: 2.0000 seconds
    """

    def __init__(self):
        """Initialize the ExecutionTimer with uninitialized start and end times."""
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        """
        Starts the timer by capturing the current time.

        Returns:
            ExecutionTimer: The current instance to access start and end times if needed.
        """
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Stops the timer and calculates the elapsed time upon exiting the context.

        Args:
            exc_type (type): Type of any exception raised within the context.
            exc_value (Exception): Exception instance raised within the context.
            traceback (traceback): Traceback object for the raised exception.

        Returns:
            bool: False to propagate any exceptions that occur during execution.
        """
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time:.4f} seconds")
        return False
