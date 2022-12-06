import multiprocessing


class NewProcess(multiprocessing.Process):
    def __init__(self):
        super().__init__()

    def run(self):
        print(f"Hello from {self.name}({self.pid})")


def new_process():
    print(f"Hello from {multiprocessing.current_process().name}({multiprocessing.current_process().pid})")


class Counter:
    def __init__(self):
        self.count = 0


class Process2ChangeCounter(multiprocessing.Process):
    def __init__(self, counter):
        super().__init__()
        self.counter = counter

    def run(self):
        print(f"[{self.pid}] Counter is {self.counter.count}")
        for i in range(1000):
            self.counter.count += 1
        print(f"[{self.pid}] Counter is {self.counter.count}")


def try_process():
    process_from_class = NewProcess()  # create a process from a class
    process_from_class.start()
    process_from_class.join()
    process_from_function = multiprocessing.Process(target=new_process)  # create a process from a function
    process_from_function.start()
    process_from_function.join()
    counter = Counter()
    process_to_change_counter = Process2ChangeCounter(counter)  # testing if the counter is shared between processes
    print(f"[{multiprocessing.current_process().pid}] Counter is {counter.count}")
    process_to_change_counter.start()
    process_to_change_counter.join()
    print(f"[{multiprocessing.current_process().pid}] Counter is {counter.count}")


if __name__ == '__main__':
    try_process()
