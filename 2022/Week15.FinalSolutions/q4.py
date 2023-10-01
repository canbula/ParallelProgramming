from multiprocessing import Process, Value


def plus_one_by_one(n: Value, times: int):
    for i in range(times):
        with n.get_lock():
            n.value += 1


def minus_one_by_one(n: Value, times: int):
    for i in range(times):
        with n.get_lock():
            n.value -= 1


if __name__ == '__main__':
    number = Value('i', 0, lock=True)
    p1 = Process(
        target=plus_one_by_one,
        args=(number, 1000000)
    )
    p2 = Process(
        target=minus_one_by_one,
        args=(number, 1000000)
    )
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(number.value)
