import threading
from functools import wraps


def threaded(number_of_threads):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            threads = []

            for _ in range(number_of_threads):
                thread = threading.Thread(
                    target=func,
                    args=args,
                    kwargs=kwargs
                )
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

        return wrapper

    return decorator
