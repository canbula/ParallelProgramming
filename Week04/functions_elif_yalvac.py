# 1. custom_power
custom_power = lambda x=0, /, e=1: x ** e



# 2. custom_equation
def custom_equation(x: int = 0, y: int = 0, /,
                    a: int = 1, b: int = 1, *,
                    c: int = 1) -> float:
    """
    Calculates a specific mathematical expression.

    :param x: positional-only integer, default 0
    :param y: positional-only integer, default 0
    :param a: positional-or-keyword integer, default 1
    :param b: positional-or-keyword integer, default 1
    :param c: keyword-only integer, default 1
    :return: result of (x**a + y**b) / c as float
    """

    for val in (x, y, a, b, c):
        if not isinstance(val, int):
            raise TypeError("must be int")
    return (x ** a + y ** b) / c



# 3. fn_w_counter
def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "count"):
        fn_w_counter.count = 0
    fn_w_counter.count += 1
    return fn_w_counter.count, {__name__.split('.')[-1]: fn_w_counter.count}
