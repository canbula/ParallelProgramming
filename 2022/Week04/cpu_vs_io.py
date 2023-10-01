import requests
import asyncio
import aiohttp
import time


class PrimeNumberGenerator:
    def __init__(self):
        self.prime_numbers = []

    @staticmethod
    def is_prime(number: int) -> bool:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __next__(self) -> int:
        if len(self.prime_numbers) == 0:
            self.prime_numbers.append(2)
            return 2
        else:
            number = self.prime_numbers[-1]
            while True:
                number += 1
                if self.is_prime(number):
                    self.prime_numbers.append(number)
                    return number

    def __iter__(self):
        return self


def primes_below(limit: int) -> list:
    with PrimeNumberGenerator() as prime_number_generator:
        primes = []
        for prime_number in prime_number_generator:
            if prime_number < limit:
                primes.append(prime_number)
            else:
                break
    return primes


def get_prime_numbers(limit: int) -> list:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/106.0.0.0 Safari/537.36'}
    with requests.request("GET", f"https://www.canbula.com/prime/{limit}",
                          headers=headers) as r:
        return r.json()["primes"]


async def get_prime_numbers_async(limit: int):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/106.0.0.0 Safari/537.36'}
    aiohttp_session = aiohttp.ClientSession()
    async with aiohttp_session.get(f"https://www.canbula.com/prime/{limit}",
                                   headers=headers,
                                   ssl=None) as r:
        p = (await r.json())["primes"]
    await aiohttp_session.close()
    return p


class MeasureAndPrint:
    def __init__(self, async_=False):
        self.async_ = async_

    def __call__(self, func):
        def _measure_and_print(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start} seconds")
            return result

        async def _measure_and_print_async(*args, **kwargs):
            start = time.time()
            result = await func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start} seconds")
            return result

        return _measure_and_print_async if self.async_ else _measure_and_print


@MeasureAndPrint()
def main():
    p = [get_prime_numbers(_) for _ in range(10)]
    return p


@MeasureAndPrint(async_=True)
async def main_async():
    p = await asyncio.gather(*[get_prime_numbers_async(_) for _ in range(10)])
    return p


if __name__ == "__main__":
    print(primes_below(10))
    print(*main())
    print(*asyncio.run(main_async()))
