def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    This function calculates a custom equation.

    :param x: first base number (default 0)
    :param y: second base number (default 0)
    :param a: exponent for x (default 1)
    :param b: exponent for y (default 1)
    :param c: divisor (default 1)
    :return: the result of (x**a + y**b) / c
    """
    return (x**a + y**b) / c

def fn_w_counter() -> (int, dict[str, int]):
    fn_w_counter.total_calls = getattr(fn_w_counter, "total_calls", 0) + 1
    callers = getattr(fn_w_counter, "callers", {})
    module_name = fn_w_counter.__module__
    callers[module_name] = callers.get(module_name, 0) + 1
    fn_w_counter.callers = callers
    return fn_w_counter.total_calls, fn_w_counter.callers
