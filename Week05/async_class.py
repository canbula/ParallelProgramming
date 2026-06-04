import asyncio
import random


class MyClass:
    def __init__(self, number):
        print(f"This call will end up with a random digit in {number} seconds")
        self.number = number

    async def method(self):
        return await asyncio.sleep(self.number, result=random.randint(0, 9))

    def __await__(self):
        return self.method().__await__()


async def main():
    my_object = MyClass(3)
    print(await my_object)
    tasks = [asyncio.create_task(MyClass(_).method()) for _ in range(10)]
    print(await asyncio.gather(*tasks))


if __name__ == '__main__':
    asyncio.run(main())
