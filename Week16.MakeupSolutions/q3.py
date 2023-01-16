import multiprocessing
import random
import time


class DaemonRandomGenerator(multiprocessing.Process):
    def __init__(self, q: multiprocessing.Queue):
        super().__init__()
        self.daemon = True
        self.q = q

    def run(self):
        while True:
            self.q.put(random.random())


def main():
    queue = multiprocessing.Queue()
    generator = DaemonRandomGenerator(queue)
    generator.start()
    while True:
        while not queue.empty():
            print(queue.get())
        time.sleep(1)


if __name__ == "__main__":
    main()
