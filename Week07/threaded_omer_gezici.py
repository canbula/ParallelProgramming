import threading
from functools import wraps
import random
import time

def threaded(n: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            threads = []

            for i in range(n):
                t = threading.Thread(target=func, args=args, kwargs=kwargs)
                threads.append(t)
                t.start()


            for t in threads:
                t.join()

            return None
        return wrapper
    return decorator
