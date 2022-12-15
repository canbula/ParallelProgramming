import multiprocessing


class PrimeFinder(multiprocessing.Process):
    def __init__(self, from_, to_, a: multiprocessing.Array):
        super().__init__()
        self.from_ = from_
        self.to_ = to_
        self.a = a

    def run(self) -> None:
        for i in range(self.from_, self.to_):
            if i == 2:
                self.a[i] = i
                continue
            # çiftse direk ele
            if i % 2 == 0:
                continue

            for j in range(2, i+1):
                if i % j == 0:
                    break
                if j == i-1:
                    self.a[i] = i


def find_primes_serial(n:int) -> list:

    a = multiprocessing.Array('i', n, lock=True)

    pf = PrimeFinder(1, n, a)
    pf.start()
    pf.join()

    return [i for i in a if i!=0]


def find_primes_parallel(n:int, process_count:int) -> list:
    
    processes = []
    a = multiprocessing.Array('i', n, lock=True)
    for i in range(process_count):
        processes.append(PrimeFinder(int(i* n/process_count),int((i+1)* n/process_count), a))
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    return [i for i in a if i!=0]
