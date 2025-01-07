import threading

def threaded(n):
    def decorator(f):
        def wrapper(*args, **kwargs):
            threads = []
            for _ in range(n):
                t = threading.Thread(
                    target=f, args=args,
                    kwargs=kwargs)
                threads.append(t)
                t.start()
            for thread in threads:
                thread.join()
        return wrapper
    return decorator
