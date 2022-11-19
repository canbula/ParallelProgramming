import threading
import random


class DaemonPi(threading.Thread):
    def __init__(self, n: int = 1000):
        super().__init__()
        self.n = n
        self.__inner = 0
        self.__total = 0

    def run(self):
        for _ in range(self.n):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            self.total += 1
            if x ** 2 + y ** 2 <= 1:
                self.inner += 1

    def pi(self):
        return 4 * self.inner / self.total


def main():
    pi_thread = DaemonPi()
    pi_thread.start()
    pi_thread.join()
    while True:
        radius = input("Enter radius: ")
        if radius == "q":
            break
        print(f"Pi is estimated as {pi_thread.pi()}")
        print(f"Area of circle with radius {radius} is "
              f"{pi_thread.pi() * float(radius) ** 2}")


if __name__ == '__main__':
    main()
