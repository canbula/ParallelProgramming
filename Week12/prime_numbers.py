import multiprocessing


def find_primes_serial(n):
    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return primes


def find_primes_parallel(end, num_of_processes):
    n = end
    m = num_of_processes
    a = multiprocessing.Array('i', n)
    processes = [PrimeFinder(i * n // m + 1, (i + 1) * n // m, a) for i in range(m)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    result = list(a)
    result.sort()
    result = [i for i in result if i != 0]
    return result


class PrimeFinder(multiprocessing.Process):
    def __init__(self, start_number, end, array):
        super().__init__()
        self.start_number = start_number
        self.end = end
        self.array = array

    def run(self) -> None:
        for i in range(self.start_number, self.end + 1):
            if is_prime(i):
                self.array[i] = i


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
