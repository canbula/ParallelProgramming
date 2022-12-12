
import multiprocessing


def find_primes_serial(n: int) -> list[int]:
    list = [0] * n
    returnlist = []
    for i in range(len(list)):
        if (is_prime(i)):
            returnlist.append(i)
    return returnlist


def find_primes_parallel(n: int, m: int) -> list[int]:
    a = multiprocessing.Array('i', [0] * n)
    final = []
    processes = [PrimeFinder(i * n // m + 1, (i + 1) * n // m, a)
                 for i in range(m)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    final = list(a)
    final.sort()
    final = [i for i in final if i != 0]
    return final


class PrimeFinder(multiprocessing.Process):
    def __init__(self, s: int, e: int, a: multiprocessing.Array):
        super().__init__()
        self.s = s
        self.e = e
        self.a = a

    def run(self):
        for i in range(self.s, self.e+1):
            if (is_prime(i)):
                self.a[i] = i


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num/2), 2):
        if (num % i) == 0:
            return False
    return True
