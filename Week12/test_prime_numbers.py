import time
import prime_numbers


# pytest -v for verbose output
# pytest -q --tb=no for no output
def test_names():
    assert callable(prime_numbers.find_primes_serial), "find_primes_serial should be a function"
    assert callable(prime_numbers.find_primes_parallel), "find_primes_parallel should be a function"
    assert "find_primes_serial" in dir(prime_numbers), "You should have a function named find_primes_serial"
    assert "find_primes_parallel" in dir(prime_numbers), "You should have a function named find_primes_parallel"
    assert "PrimeFinder" in dir(prime_numbers), "You should have a class named PrimeFinder"
    assert "multiprocessing" in dir(prime_numbers), "You should import multiprocessing"


def test_serial():
    assert isinstance(prime_numbers.find_primes_serial(100), list), "find_primes_serial should return a list"
    assert prime_numbers.find_primes_serial(10) == [
        2, 3, 5, 7
    ], "find_primes_serial should return the correct list of primes"
    assert prime_numbers.find_primes_serial(90) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89
    ], "find_primes_serial should return the correct list of primes"
    assert prime_numbers.find_primes_serial(900) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
        101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
        211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
        307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
        401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
        601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
        701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
        809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887
    ], "find_primes_serial should return the correct list of primes"
    assert len(prime_numbers.find_primes_serial(100000)) == 9592, \
        "find_primes_serial should return the correct list of primes"


def test_parallel():
    assert isinstance(prime_numbers.find_primes_parallel(100, 2), list), "find_primes_parallel should return a list"
    assert prime_numbers.find_primes_parallel(10, 2) == [
        2, 3, 5, 7
    ], "find_primes_parallel should return the correct list of primes"
    assert prime_numbers.find_primes_parallel(100, 2) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ], "find_primes_parallel should return the correct list of primes"
    assert prime_numbers.find_primes_parallel(1000, 4) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
        101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
        211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
        307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
        401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
        601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
        701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
        809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
        907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
    ], "find_primes_parallel should return the correct list of primes"
    assert len(prime_numbers.find_primes_parallel(100000, 4)) == 9592, \
        "find_primes_parallel should return the correct list of primes"
    assert len(prime_numbers.find_primes_parallel(100000, 8)) == 9592, \
        "find_primes_parallel should return the correct list of primes"


def test_speed():
    start = time.time()
    prime_numbers.find_primes_serial(1_000_000)
    serial_time = time.time() - start
    start = time.time()
    prime_numbers.find_primes_parallel(1_000_000, 4)
    parallel_time = time.time() - start
    assert parallel_time < serial_time, "find_primes_parallel should be faster than find_primes_serial"


def test_multiprocessing():
    import multiprocessing
    n = 100000
    m = 4
    a = multiprocessing.Array('i', n)
    processes = [prime_numbers.PrimeFinder(i * n // m + 1, (i + 1) * n // m, a) for i in range(m)]
    for p in processes:
        p.start()
    number_of_processes = multiprocessing.active_children()
    for p in processes:
        p.join()
    assert len(number_of_processes) == m, "find_primes_parallel should use multiprocessing"
