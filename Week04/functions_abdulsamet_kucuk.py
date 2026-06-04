custom_power = lambda x=0, /, e=1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the custom equation (x**a + y**b) / c.

    :param x: The first base value (positional-only).
    :param y: The second base value (positional-only).
    :param a: The first exponent value (positional-or-keyword).
    :param b: The second exponent value (positional-or-keyword).
    :param c: The divisor (keyword-only).
    :return: The result of the custom equation as a float.
    """
    for param in (x, y, a, b, c):
        if not isinstance(param, int) or isinstance(param, bool):
            raise TypeError("All parameters must be integers.")

    return float((x**a + y**b) / c)

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.callers = {}

    caller_name = __name__

    fn_w_counter.total_calls += 1
    fn_w_counter.callers[caller_name] = fn_w_counter.callers.get(caller_name, 0) + 1

    return fn_w_counter.total_calls, fn_w_counter.callers
