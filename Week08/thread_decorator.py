import threading


class MakeThreads:
    def __init__(self, n: int = 1):
        self.n = n
        self.threads = []

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.n):
                t = threading.Thread(target=func, args=args, kwargs=kwargs)
                self.threads.append(t)
                t.start()
            for t in self.threads:
                t.join()
        return wrapper


@MakeThreads(4)
def main():
    print(f"Hello from thread {threading.get_ident()}")


if __name__ == '__main__':
    main()
