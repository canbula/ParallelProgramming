import threading
import random
import math


class DaemonPi(threading.Thread):
    def __init__(self, n: int = 1000):
        super().__init__(daemon=True) # Fixes the open github issue #7
        self.n = n
        self._inner = 0 # Fixes the open github issue #8
        self._total = 0 # Fixes the open github issue #8
        self.lock = threading.Lock()


    def run(self):
        while True: # Fixes the open github issue #9
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            with self.lock: # Fixes the open github issue #10
                # Put the thread to sleep to allow the main thread to run
                # time.sleep(0.0000001) # Fixes the open github issue #13
                self._total += 1
                if x ** 2 + y ** 2 <= 1:
                    self._inner += 1


    def pi(self):
        with self.lock: # Fixes the open github issue #12
            return 4 * self._inner / self._total


    def get_total_inner(self):
        """Returns a copy of the _total and _inner values by using the lock."""
        with self.lock:
            return self._total, self._inner


    @staticmethod
    def calculate_radius(pi, radius):
        return pi * (float(radius) ** 2)


    def get_current_progress(self, radius):
        # Generate a progress bar with the _total and _inner values

        total_local, inner_local = self.get_total_inner()
        estimated_pi = self.pi()

        progress_str = \
f"""
Gathered {total_local} points, and {inner_local} of them are inside the circle.
* Estimated Value of PI: {estimated_pi:.30f}
* Real Value of PI     : {math.pi:.30f}
---------------------------------------------------------
* Estimated Radius of the circle: {self.calculate_radius(pi=estimated_pi, radius=radius):.10f}
* Real      Radius of the circle: {self.calculate_radius(pi=math.pi, radius=radius):.10f}

"""
        print("\033c", end="") # Clears the terminal
        print(progress_str, end="\r") # Prints the progress string


def main():
    pi_thread = DaemonPi()
    pi_thread.start()
    # Removed pi_thread.join() to avoid blocking the main thread, which fixes the open github issue #11
    while True:
        radius = input("\nEnter radius: ")
        if str(radius).strip().lower() == "q":
            break

        try: # Validates if the user input is a floating number.
            radius = float(radius)
        except ValueError:
            print("Please enter a valid float value for the radius. | q to quit")
            continue

        pi_thread.get_current_progress(radius=radius)


if __name__ == '__main__':
    main()
