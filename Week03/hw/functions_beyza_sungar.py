custom_power = lambda x=0 ,/, e=1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    This function returns (x**a + y**b)/c.
    :param x: First number
    :param y: Second number
    :param a: First exponent
    :param b: Second exponent
    :param c : Third number
    :return: (x**a + y**b)/c
    """

    return float((x**a +y**b)/c)

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "call_counter"):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_counts = {}

    caller_name = __name__
    fn_w_counter.call_counter += 1

    if caller_name in fn_w_counter.caller_counts:
        fn_w_counter.caller_counts[caller_name] += 1
    else:
        fn_w_counter.caller_counts[caller_name] = 1

    return fn_w_counter.call_counter, fn_w_counter.caller_counts
