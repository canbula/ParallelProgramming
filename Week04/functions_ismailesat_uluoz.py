custom_power = lambda x=0, /, e=1: x ** e


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
    Computes a custom mathematical expression.

    :param x: Positional-only integer, default 0
    :param y: Positional-only integer, default 0
    :param a: Exponent for x, default 1
    :param b: Exponent for y, default 1
    :param c: Divisor (keyword-only), default 1
    :return: Computed float result
    :rtype: float
    """
    return (x**a + y**b) / c


def fn_w_counter() -> tuple[int, dict[str, int]]:
    if not hasattr(fn_w_counter, "count"):
        fn_w_counter.count = 0

    if not hasattr(fn_w_counter, "history"):
        fn_w_counter.history = {}

    name = __name__

    fn_w_counter.count += 1

    if name in fn_w_counter.history:
        fn_w_counter.history[name] += 1
    else:
        fn_w_counter.history[name] = 1

    return fn_w_counter.count, fn_w_counter.history
