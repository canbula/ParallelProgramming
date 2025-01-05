import threading

def run_in_threads(thread_count):
    """
    A decorator to execute a function concurrently in multiple threads.

    This decorator allows the decorated function to run `thread_count` times
    concurrently in separate threads with the same arguments.

    Parameters
    ----------
    thread_count : int
        The number of threads to spawn for executing the function.

    Returns
    -------
    ThreadManager
        A decorator class that manages the thread lifecycle.

    Examples
    --------
    >>> @run_in_threads(3)
    ... def sample_task(data):
    ...     print(f"Processing: {data}")
    ...
    >>> sample_task("example")
    Processing: example
    Processing: example
    Processing: example

    Notes
    -----
    - Each thread runs the same function with the same parameters.
    - The function waits for all threads to complete before proceeding.
    - Return values from the threads are not captured.
    """
    class ThreadManager:
        def __init__(self, thread_count):
            self.thread_count = thread_count

        def __call__(self, func):
            def wrapper(*args, **kwargs):
                threads = []
                for _ in range(self.thread_count):
                    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
                    threads.append(thread)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()
            return wrapper
    return ThreadManager(thread_count)
