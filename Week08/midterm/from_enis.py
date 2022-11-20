import random
import threading
from numba import jit
import time
import os


def see_threads():
    while True:
        for t in threading.enumerate():
            print(t.name, end=' ')
        print()
        time.sleep(0.5)



class RandomNumberGenerator(threading.Thread):
    """
    A class to find natural number "e" (Eular's number) by using multi thread.
    To learn how to find the constat "e" watch :
     From minute 52.45 to end of to the given link:
      https://www.youtube.com/watch?v=Y_o5768i5hA&list=PL30NBs02RsiUbmXVPDo56APsU0xa6gfL2&index=3
    """
    def __init__(self, num_n, index):
        super().__init__()
        self.num_n = num_n # The amount of numbers that are going to be generated and used to find natural number 'e'.
        self.index = index # Index numbers for the threads.
        self.avg_of_sum = 0 # The average of numbers that are generated.Also represents the Eular's number that is founded by indexed thread.

    def run(self):
        self.avg_of_sum = self.generate_numbers(self.num_n)
        print(f"Thread {self.index} finished and generated {self.num_n} numbers")
        print(f"Thread {self.index} generated Eular's number (constant e) as : {self.avg_of_sum}")
        print("")

    @staticmethod
    @jit(nopython=True, nogil=True)
    def generate_numbers(num_n):
        n_list = []
        for j in range(num_n):
            sum_x = 0
            for i in range(10):
                x = random.uniform(0, 1)
                if sum_x < 1:
                    sum_x += x
                else:
                    index_number = i
                    n_list.append(index_number)
                    break
        return sum(n_list)/len(n_list)


def main():
    t = threading.Thread(target=see_threads, daemon=True) # The daemon thread to see which threads are alive.
    t.start()
    num_n = 50000000
    num_threads = os.cpu_count()
    threads = []
    for i in range(num_threads):
        t = RandomNumberGenerator(num_n, i)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    number_e = sum(t.avg_of_sum for t in threads)/num_threads
    print(f"Totally {num_n * num_threads} numbers generated")
    print("")
    print(f"The final Eular's number (constant e) is generated as : {number_e} ")


if __name__ == '__main__':
    main()
