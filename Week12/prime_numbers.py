import multiprocessing
import math

def is_prime(n):
        if n <= 1:
            return False
        return all(n % i != 0 for i in range(2, 1 + math.floor(math.sqrt(n))))

def find_primes_serial(n: int) -> list[int]:
    return [i for i in range(2, n) if is_prime(i)]

def find_primes_parallel(n: int, m: int) -> list[int]:
    array = multiprocessing.Array('i', range(2, n), lock=False)
    processes = []
    for i in range(m):
        start = i * n // m
        end = (i + 1) * n // m
        processes.append(PrimeFinder(start, end, array))
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return [index for index in range(len(array)) if array[index] == 1]


class PrimeFinder(multiprocessing.Process):
    def __init__(self, start: int, end: int, array: multiprocessing.Array):
        super().__init__()
        self.start_ = start
        self.end = end
        self.array = array

    def run(self) -> None:
        for i in range(self.start_, self.end):
            if is_prime(i):
                self.array[i] = 1