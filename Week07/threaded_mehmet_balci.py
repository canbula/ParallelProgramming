from concurrent.futures import ThreadPoolExecutor

def threaded(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with ThreadPoolExecutor(max_workers=n) as executor:
                for _ in range(n):
                    executor.submit(func, *args, **kwargs)
        return wrapper
    return decorator
