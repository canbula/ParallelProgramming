import threading

def threaded(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []
            results = [None] * n
            errors = [None] * n

            def worker(i):
                try:
                    results[i] = func(*args, **kwargs)
                except Exception as e:
                    errors[i] = e

            for i in range(n):
                t = threading.Thread(target=worker, args=(i,))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

            if any(errors):
                raise Exception(errors)

            return results

        return wrapper
    return decorator
