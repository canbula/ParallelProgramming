import time

class Timer:
    """
    This class calculates the time taken by a piece of code.

    Attributes
    ----------
    start_time : float
        The start time of the block of code.
    end_time : float
        The end time of the block of code.
    elapsed_time : float
        The total time taken by the code block (in seconds).

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
        Initializes an instance of Timer.

        Returns:
            None
        """
        print(f"Initializing {self.__class__.__name__}")
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None  # Initialize elapsed_time attribute

    def __enter__(self) -> "Timer":
        """
        Starts the timer by recording the start time.

        Returns:
            Timer: Returns itself
        """
        print(f"Entering {self.__class__.__name__}")
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Stops the timer, calculates the execution time, and prints it.

        Args:
            exc_type: The type of exception raised, if any.
            exc_val: The value of the exception, if any.
            exc_tb: The traceback of the exception, if any.

        Returns:
            bool: True, to suppress any exception that occurs within the context.
        """
        print(f"Exiting {self.__class__.__name__}")
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time  # Calculate and store elapsed time
        print(f"Execution time: {self.elapsed_time:.4f} seconds")
        return True

    def __call__(self, task: str) -> None:
        """
        Prints the name of the task being executed.

        Args:
            task (str): A string representing the task name.
        """
        print(f"Calling {task}")
        return None


def main() -> None:
    with Timer() as calc:
        for i in range(10 * 1000):
            i ** 0.254444


if __name__ == "__main__":
    main()
