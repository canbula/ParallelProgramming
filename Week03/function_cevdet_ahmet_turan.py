custom_power = lambda x, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, a: int = 1, b: int = 1, c: int = 1) -> float:
    """
    Compute the result of the custom equation.

    :param x: First integer (positional-only, default 0).
    :param y: Second integer (positional-only, default 0).
    :param a: Exponent for 'x' (positional-or-keyword, default 1).
    :param b: Exponent for 'y' (positional-or-keyword, default 1).
    :param c: Divisor (keyword-only, default 1).
    :return: Result of (x**a + y**b) / c as a float.
    """
    result = (x ** a + y ** b) / c
    return float(result)

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
    if not hasattr(fn_w_counter, "_dict"):
        fn_w_counter._dict = {}
    
    caller_name = __name__

    fn_w_counter.call_count += 1

    if caller_name in fn_w_counter._dict:
        fn_w_counter._dict[caller_name] += 1
    else:
        fn_w_counter._dict[caller_name] = 1

    return fn_w_counter.call_count, fn_w_counter._dict
