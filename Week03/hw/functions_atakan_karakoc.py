custom_power = lambda x = 0, /, e = 1 : x**e

def custom_equation(x : int = 0, y: int = 0, /, a : int = 1, b : int = 1, *, c : int = 1) -> float:
    """
    This function adds power a of variable x and power b of variable y. Divides the result by variable c.
    :param x: First base
    :param y: Second base
    :param a: First exponent
    :param b: Second exponent
    :param c: Divisior number
    :return: Returns the result of the operation as a float
    """
    return (x**a + y**b) / c


def fn_w_counter() -> (int, dict[str, int]):

    caller_name = globals()['__name__']

    if not hasattr(fn_w_counter, "call_counter"):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_counts = {}

    fn_w_counter.call_counter += 1

    if caller_name in fn_w_counter.caller_counts:
        fn_w_counter.caller_counts[caller_name] += 1
    else:
        fn_w_counter.caller_counts[caller_name] = 1

    return fn_w_counter.call_counter, fn_w_counter.caller_counts

