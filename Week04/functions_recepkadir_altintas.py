
custom_power = lambda x=0, /, e=1: x**e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the mathematical equation.

    :param x: The first base value.
    :param y: The second base value.
    :param a: The exponent for x.
    :param b: The exponent for y.
    :param c: The divisor.
    :return: The result of the equation.
    """

    if not all(isinstance(arg, int) for arg in (x, y, a, b, c)):
        raise TypeError("All arguments must be integers.")

    return float((x**a + y**b) / c)


def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.caller_info = {}

    fn_w_counter.total_calls += 1

    caller_name = __name__

    fn_w_counter.caller_info[caller_name] = fn_w_counter.caller_info.get(caller_name, 0) + 1

    return fn_w_counter.total_calls, fn_w_counter.caller_info.copy()
