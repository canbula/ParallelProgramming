import time

class Timer:
    """
    A class that measures the time taken by a block of code.

    This class implements a context manager that tracks the execution time
    of the code within the context block. It also provides a callable
    method to print the name of the task being executed.

    :ivar start_time: The start time of the block of code.
    :ivar end_time: The end time of the block of code.

    Methods
    -------
    __enter__():
        Records the start time and enters the context.
    __exit__(exc_type, exc_val, exc_tb):
        Records the end time, calculates the execution time, and exits the context.
    __call__(task: str):
        Prints the name of the task being executed.
    """

    def __init__(self) -> None:
        """
        Initializes the Timer class and sets the start and end times to None.
        """
        print(f"Initializing {self.__class__.__name__}")
        self.start_time = None
        self.end_time = None

    def __enter__(self) -> "Timer":
        """
        Starts the timer by recording the start time.

        :returns: The Timer instance itself.
        """
        print(f"Entering {self.__class__.__name__}")
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Stops the timer, calculates the execution time, and prints it.

        :param exc_type: The type of exception raised, if any.
        :param exc_val: The value of the exception, if any.
        :param exc_tb: The traceback of the exception, if any.
        :returns: True, to suppress any exception that occurs within the context.
        """
        print(f"Exiting {self.__class__.__name__}")
        self.end_time = time.time()
        execution_time = self.end_time - self.start_time
        print(f"Execution time: {execution_time:.4f} seconds")
        return True

    def __call__(self, task: str) -> None:
        """
        Prints the name of the task being executed.

        :param task: A string representing the task name.
        """
        print(f"Calling {task}")
        return None


def main() -> None:
    """
    Example usage of the Timer class.

    A simple task that runs within the Timer context to measure its execution time.
    """
    with Timer() as cm:
        cm("example task")


if __name__ == "__main__":
    main()
