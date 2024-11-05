import time

class Timer:
    """
    A context manager to measure the time taken for a block of code to execute.

    Attributes:
        start_time (float): The start time of the code block.
        end_time (float): The end time of the code block.
    """

    def __init__(self):
        """
        Initializes the Timer class with start_time and end_time set to 0.
        """
        self.start_time = 0
        self.end_time = 0

    def __enter__(self):
        """
        Starts the timer.

        Returns:
            Timer: Returns the Timer instance with start_time set to the current time.
        """
        self.start_time = time.time()
        return self

    def __exit__(self, *kwargs):
        """
        Stops the timer by setting end_time to the current time.
        """
        self.end_time = time.time()

if __name__ == "__main__":
    with Timer() as timer:
        print(timer.start_time)
        time.sleep(2)
    print(timer.end_time)
