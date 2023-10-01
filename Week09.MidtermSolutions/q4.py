import threading
from math import factorial
import time


class EstimateEuler(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.lock = threading.Lock()
        self.__e = 0

    def run(self):
        i = 0
        while True:
            with self.lock:
                self.__e += 1 / factorial(i)
                i += 1
            time.sleep(1)

    def value(self):
        with self.lock:
            return self.__e


def main():
    e = EstimateEuler()
    e.start()
    while True:
        time.sleep(1)
        print(e.value())


if __name__ == '__main__':
    main()
