import multiprocessing
import random


class ValueChanger(multiprocessing.Process):
    def __init__(self, value_instance):
        super().__init__()
        self.value_instance = value_instance

    def run(self):
        self.value_instance.value = random.randint(0, 100)


class ValuePlus(multiprocessing.Process):
    def __init__(self, value_instance):
        super().__init__()
        self.value_instance = value_instance

    def run(self):
        for i in range(100000):
            #  self.value_instance.value += 1
            with self.value_instance.get_lock():
                self.value_instance.value += 1


class ValueMinus(multiprocessing.Process):
    def __init__(self, value_instance):
        super().__init__()
        self.value_instance = value_instance

    def run(self):
        for i in range(100000):
            #  self.value_instance.value -= 1
            with self.value_instance.get_lock():
                self.value_instance.value -= 1


class ArrayRandomizer(multiprocessing.Process):
    def __init__(self, array_instance):
        super().__init__()
        self.array_instance = array_instance

    def run(self):
        for i in range(len(self.array_instance)):
            self.array_instance[i] = random.random()


def try_value():
    value_instance = multiprocessing.Value('i', 0, lock=True)
    process = ValueChanger(value_instance)
    process.start()
    process.join()
    print(value_instance.value)
    other_value_instance = multiprocessing.Value('i', value_instance.value, lock=True)
    processes = [ValuePlus(other_value_instance), ValueMinus(other_value_instance)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(other_value_instance.value)


def try_array():
    array_instance = multiprocessing.Array('d', 10, lock=True)
    process = ArrayRandomizer(array_instance)
    process.start()
    process.join()
    print(*[f"{x:.2f}" for x in array_instance[:]])


if __name__ == '__main__':
    try_value()
    try_array()
