custom_power = lambda x = 0, /, e = 1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """This function returns a float value of the equation (x ** a + y ** b) / c

    :param x: The first term of the equation. Default is 0.
    :param y: The second term of the equation. Default is 0.
    :param a: The exponent for the first term of the equation. Default is 1.
    :param b: The exponent for the second term of the equation. Default is 1.
    :param c: The divisor for the entire equation. Default is 1.
    :return: The result of the equation (x ** a + y ** b) / c as a float.
    """
    return (custom_power(x, e = a) + custom_power(y, e = b)) / c

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = 0
        fn_w_counter.callers = {}
    fn_w_counter.counter += 1
    caller_name = __name__
    if caller_name in fn_w_counter.callers:
        fn_w_counter.callers[caller_name] += 1
    else:
        fn_w_counter.callers[caller_name] = 1
    return fn_w_counter.counter, fn_w_counter.callers
