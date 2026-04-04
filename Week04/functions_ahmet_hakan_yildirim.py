from typing import Tuple, Dict

custom_power = lambda x=0, /, e=1: (x ** e)


def custom_equation(
    x: int = 0,
    y: int = 0,
    /,
    a: int = 1,
    b: int = 1,
    *,
    c: int = 1
) -> float:
    """
    :param x: positional-only
    :param y: positional-only
    :param a: positional or keyword
    :param b: positional or keyword
    :param c: keyword-only
    :return: result as float
    """

    values = [x, y, a, b, c]

    for v in values:
        if not isinstance(v, int):
            raise TypeError("Arguments must be integers")

    numerator = (x ** a + y ** b)
    result = numerator / c

    return float(result)


def fn_w_counter() -> Tuple[int, Dict[str, int]]:
    if getattr(fn_w_counter, "count", None) is None:
        fn_w_counter.count = 0

    fn_w_counter.count += 1

    module_name = __name__.split('.')[-1]

    return fn_w_counter.count, {module_name: fn_w_counter.count}
