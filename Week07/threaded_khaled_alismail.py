import threading
import time
from functools import wraps


def create_threads(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            threads = []

            # Create and start n threads
            for i in range(n):
                t = threading.Thread(target=func, args=args, kwargs=kwargs)
                threads.append(t)
                t.start()

            # Wait for all threads to finish
            for t in threads:
                t.join()

        return wrapper
    return decorator


@create_threads(5)
def task():
    print(f"Running in thread: {threading.current_thread().name}")
    time.sleep(1)


task()
