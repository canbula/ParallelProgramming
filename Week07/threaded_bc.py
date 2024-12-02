import threading


def threaded(n):
    def decorator(func):
        def _decorator(*args, **kwargs):
            threads = []
            for i in range(n):
                t = threading.Thread(target=func, args=args, kwargs=kwargs)
                threads.append(t)
                # print(f"Threaded started thread {i+1} of {n} for {func.__name__}")
                t.start()
            for t in threads:
                t.join()

        return _decorator

    return decorator


if __name__ == "__main__":

    @threaded(3)
    def a():
        print("a")

    @threaded(2)
    def b():
        print("b")

    @threaded(4)
    def c():
        print("c")

    @threaded(1)
    def d():
        print("d")

    a()
    b()
    c()
    d()
