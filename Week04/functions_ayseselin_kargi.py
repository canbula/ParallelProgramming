custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(x: int = 0, y: int = 0, /,
                    a: int = 1, b: int = 1, *,
                    c: int = 1) -> float:
    """
    Computes a custom equation.

    :param x: positional-only
    :param y: positional-only
    :param a: positional or keyword
    :param b: positional or keyword
    :param c: keyword-only
    :return: result as float
    """

    for val in (x, y, a, b, c):
        if not isinstance(val, int):
            raise TypeError("Arguments must be integers")

    return float((x ** a + y ** b) / c)


def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "count"):
        fn_w_counter.count = 0

    fn_w_counter.count += 1

    module_name = __name__.split('.')[-1]

    return fn_w_counter.count, {module_name: fn_w_counter.count}
