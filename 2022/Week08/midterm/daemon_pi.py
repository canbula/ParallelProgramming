import threading
import random


class DaemonPi(threading.Thread):
    def __init__(self, n: int = 1000):
        super().__init__(daemon=True)  # Fixes the open GitHub issue #7
        self.n = n
        # leading double underscore makes the variable private
        self.__inner = 0  # Fixes the open GitHub issue #8
        self.__total = 0  # Fixes the open GitHub issue #8
        self.lock = threading.Lock()
        self.__loop = True  # Fixes the open GitHub issue #13

    def run(self):
        while True:  # Fixes the open GitHub issue #9
            if not self.__loop:  # Fixes the open GitHub issue #13
                continue  # Fixes the open GitHub issue #13
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            with self.lock:  # Fixes the open GitHub issue #10
                self.__total += 1
                if x ** 2 + y ** 2 <= 1:
                    self.__inner += 1

    def pi(self):
        self.__loop = False  # Fixes the open GitHub issue #13
        with self.lock:  # Fixes the open GitHub issue #12
            self.__loop = True  # Fixes the open GitHub issue #13
            print(f"Total: {self.__total}, Inner: {self.__inner}")
            return 4 * self.__inner / self.__total


def main():
    pi_thread = DaemonPi()
    pi_thread.start()
    # Removed pi_thread.join() to avoid blocking the main thread, which fixes the open GitHub issue #11
    while True:
        radius = input("\nEnter radius: ")
        if str(radius).strip().lower() == "q":
            break

        try:  # Validates if the user input is a floating number.
            radius = float(radius)
        except ValueError:
            print("Please enter a valid float value for the radius. | q to quit")
            continue

        print(f"Area of circle with radius {radius} is {pi_thread.pi() * radius ** 2}")


if __name__ == '__main__':
    main()
