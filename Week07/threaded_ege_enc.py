import threading

def threader(n: int):
    """
    This function is a decorator which takes an integer n as an argument
    and returns a threaded function.

    :param n: Number of threads
    :return: Threaded function
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []
            for _ in range(n):
                t = threading.Thread(target=func, args=args, kwargs=kwargs)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        return wrapper
    return decorator

@threader(4)
def func(value):
    print(f"Hello World: {value}")

# Test
func("dummy")
