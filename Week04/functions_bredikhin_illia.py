custom_power = lambda x=0, /, e=1: pow(x, e)


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    :param x:
    :param y:
    :param a:
    :param b:
    :param c:
    :return:
    """
    for name, value in (("x", x), ("y", y), ("a", a), ("b", b), ("c", c)):
        if type(value) is not int:
            raise TypeError(f"{name} must be int")

    result = pow(x, a) + pow(y, b)

    return float(result / c)


_count = 0


def fn_w_counter() -> (int, dict[str, int]):
    global _count

    _count = _count + 1

    return _count, dict({__name__: _count})
