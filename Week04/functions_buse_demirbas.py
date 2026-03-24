import sys

custom_power = lambda x=0, /, e=1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates (x**a + y**b) / c.
    :param x: base x
    :param y: base y
    :param a: exp a
    :param b: exp b
    :param c: div c
    :return: float result
    """

    if not all(isinstance(v, int) for v in (x, y, a, b, c)):
        raise TypeError("Arguments must be integers")
    return float((x**a + y**b) / c)


def fn_w_counter() -> tuple[int, dict[str, int]]:

    if not hasattr(fn_w_counter, "count"):
        fn_w_counter.count = 0
    
    fn_w_counter.count += 1
    module_name = __name__.split('.')[-1]
    return fn_w_counter.count, {module_name: fn_w_counter.count}
