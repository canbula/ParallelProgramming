def d1(fn):
    def _d1():
        print("Before")
        fn()
        print("After")

    return _d1


@d1
def f1():
    print("Function")


f1()
