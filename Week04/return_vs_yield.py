def returning_squares(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

def yielding_squares(n):
    for i in range(n):
        yield i**2

class Squares:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        result = self.i**2
        self.i += 1
        return result

def student_status():
    yield "Freshman"
    yield "Sophomore"
    yield "Junior"
    yield "Senior"
    


if __name__ == "__main__":
    print(type(returning_squares(5)))
    print(type(yielding_squares(5)))
    print(type(Squares(5)))

    print(dir(returning_squares(5)))
    print(dir(yielding_squares(5)))

    print(returning_squares(5))
    print(yielding_squares(5))
    print(Squares(5))

    i = yielding_squares(5)
    print(next(i), next(i), next(i), next(i), next(i))
    try:
        print(next(i))
    except StopIteration:
        print("End of iteration")

    for i in returning_squares(5):
        print(i, end=' ')
    print()

    for i in yielding_squares(5):
        print(i, end=' ')
    print()

    for i in Squares(5):
        print(i, end=' ')
    print()

    squares = Squares(5)
    print(next(squares))
    print(next(squares))
    print(next(squares))
    print(next(squares))
    print(next(squares))
    try:
        print(next(squares))
    except StopIteration:
        print("End of iteration")
    
    for status in student_status():
        print(status, end=' ')
