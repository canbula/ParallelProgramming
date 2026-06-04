custom_power = lambda x=0, /, e=1: float(x ** e)


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates (x**a + y**b) / c

    :param x: base for the first term
    :param y: base for the second term
    :param a: exponent for the first term
    :param b: exponent for the second term
    :param c: divisor for the sum
    :return: the result of the equation as float
    """
    if type(x) is not int: raise TypeError("x must be int")
    if type(y) is not int: raise TypeError("y must be int")
    if type(a) is not int: raise TypeError("a must be int")
    if type(b) is not int: raise TypeError("b must be int")
    if type(c) is not int: raise TypeError("c must be int")
    return float((x ** a + y ** b) / c)

_total = 0
_counts = {}


def fn_w_counter() -> (int, dict[str, int]):
    global _total
    _total += 1
    caller = __name__
    _counts[caller] = _counts.get(caller, 0) + 1

    return _total, _counts
