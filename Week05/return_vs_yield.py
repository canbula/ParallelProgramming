def returning_squares(n):
    return [i**2 for i in range(1, n + 1)]


def yielding_squares(n):
    for i in range(1, n + 1):
        yield i**2


def custom_yield(n):
    for i in range(1, n + 1):
        yield [i**2, (i + 1) ** 2, (i + 2) ** 2]


class Squares:
    def __init__(self, n):
        self.__n = n
        self.__i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i > self.__n:
            raise StopIteration
        result = self.__i**2
        self.__i += 1
        return result

    def set_i(self, i):
        if i < 1:
            raise ValueError
        self.__i = i

    def get_i(self):
        if not __name__ == "__main__":
            raise Exception("No access")
        return self.__i


if __name__ == "__main__":
    print(returning_squares(5))
    squares = yielding_squares(5)
    print(next(squares))
    print(next(squares))
    print(next(squares))
    print(next(squares))
    print(next(squares))
    custom_squares = custom_yield(10)
    while True:
        try:
            print(next(custom_squares))
        except StopIteration:
            print("The end")
            break
    print(dir(returning_squares))
    print(dir(squares))
    squares_obj = Squares(10)
    print(next(squares_obj))
    print(next(squares_obj))
    print(next(squares_obj))
    print(squares_obj.get_i())
    squares_obj.set_i(1)
    print(next(squares_obj))
    print(squares_obj.get_i())
