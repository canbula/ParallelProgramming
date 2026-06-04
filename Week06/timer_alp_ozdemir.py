import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
    def __enter__(self):
        print(f"Entering  {self.__class__.__name__}")
        self.start_time = time.time()
        return self
    def __call__(self,task : str):
        print(f"Calling {task}")
        return self.end_time - self.start_time
    def __exit__(self,exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        return False

def main():
    with Timer() as T:
        T("go")

if __name__ == "__main__":
    main()
