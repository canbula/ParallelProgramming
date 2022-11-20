import threading
import random
import time

class DaemonPi(threading.Thread):
    def __init__(self, n: int = 1000):
        super().__init__()
        self.n = n
        self.__inner = 0
        self.__total = 0
        self.daemon = True
        self.lock = threading.Lock()

    def run(self):
        while True:
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            with self.lock:
                self.__total += 1
                if x ** 2 + y ** 2 <= 1:
                    self.__inner += 1
            time.sleep(.2) # wait for a possible pi calculation request

    def pi(self):
        with self.lock:
            return 4 * self.__inner / self.__total


def main():
    pi_thread = DaemonPi()
    pi_thread.start()
    while True:
        radius = input("Enter radius: ")
        if radius == "q":
            break
        print(f"Pi is estimated as {pi_thread.pi()}")
        print(f"Area of circle with radius {radius} is "
              f"{pi_thread.pi() * float(radius) ** 2}")

if __name__ == '__main__':
    main()
