from functools import wraps
from threading import Thread


def threaded(n: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            threads = []

            for _ in range(n):
                thread = Thread(target=func, args=args, kwargs=kwargs)
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

        return wrapper

    return decorator