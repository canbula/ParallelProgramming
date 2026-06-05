import threading
from functools import wraps

def execute_in_threads(thread_total: int):
    """
    A decorator that runs the decorated function in multiple threads.
    It manages thread creation, execution, and synchronization.
    """

    def decorator(target_func):

        @wraps(target_func)
        def wrapper(*func_args, **func_kwargs):
            workers = []

            # Create threads
            for _ in range(thread_total):
                thread = threading.Thread(
                    target=target_func,
                    args=func_args,
                    kwargs=func_kwargs
                )
                workers.append(thread)

            # Start all threads
            for thread in workers:
                thread.start()

            # Wait for all threads to complete
            for thread in workers:
                thread.join()

        return wrapper

    return decorator
