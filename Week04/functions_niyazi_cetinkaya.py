custom_power = lambda x = 0, /, e = 1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculate a custom equation based on the provided parameters.

    The function computes the result of the equation:
    (x**a + y**b) / c

    :param x: The first integer value (positional-only, default is 0).
    :param y: The second integer value (positional-only, default is 0).
    :param a: The exponent for x (positional or keyword, default is 1).
    :param b: The exponent for y (positional or keyword, default is 1).
    :param c: The divisor (keyword-only, default is 1).
    :return: The result of the equation as a float.
    """
    return (x**a + y**b) / c

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "call_counter"):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_count_dict = {}

    caller = __name__
    fn_w_counter.call_counter += 1

    if caller not in fn_w_counter.caller_count_dict:
        fn_w_counter.caller_count_dict[caller] = 1
    else:
        fn_w_counter.caller_count_dict[caller] += 1

    return fn_w_counter.call_counter, fn_w_counter.caller_count_dict
