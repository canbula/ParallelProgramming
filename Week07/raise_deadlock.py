import threading


class Deadlock(threading.Thread):
    def __init__(self, lock1, lock2):
        super().__init__()
        self.lock1 = lock1
        self.lock2 = lock2

    def run(self):
        with self.lock1:
            print(f"Thread {self.name} acquired lock1")
            with self.lock2:
                print(f"Thread {self.name} acquired lock2")


def main():
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    t1 = Deadlock(lock1, lock2)
    t2 = Deadlock(lock2, lock1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
