import threading


def threaded(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []

            for _ in range(n):
                t = threading.Thread(target=func, args=args, kwargs=kwargs)
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

        return wrapper
    return decorator
