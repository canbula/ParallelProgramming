import sys


def _custom_power(x=0, /, e=1):
    return x**e

_custom_power.__name__ = "<lambda>"
custom_power = _custom_power


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates (x**a + y**b) / c.

    :param x: first number
    :param y: second number
    :param a: power of x
    :param b: power of y
    :param c: divides the result
    :return: float result
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if not isinstance(y, int):
        raise TypeError("y must be an integer")
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    if not isinstance(c, int):
        raise TypeError("c must be an integer")
    return (x**a + y**b) / c


def fn_w_counter() -> (int, dict[str, int]):
    caller = sys._getframe(0).f_globals.get("__name__", "__main__")
    fn_w_counter.total += 1
    if caller not in fn_w_counter.callers:
        fn_w_counter.callers[caller] = 0
    fn_w_counter.callers[caller] += 1
    return (fn_w_counter.total, dict(fn_w_counter.callers))

fn_w_counter.total = 0
fn_w_counter.callers = {}
