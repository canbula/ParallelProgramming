custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    This function raises x to the power of a, y to the power of b,
    sums them, and then divides the result by c.

    :param x: The positional-only integer base parameter
    :param y: The positional-only integer base parameter
    :param a: The exponent for x
    :param b: The exponent for y
    :param c: The divisor (keyword-only)
    :return: (x**a + y**b) / c
    :rtype: float
    """
    return (x ** a + y ** b) / c


def fn_w_counter() -> tuple[int, dict[str, int]]:
    """
    Counts how many times this function is called and records
    how many calls came from each module.
    """
    if not hasattr(fn_w_counter, '_call_counter'):
        fn_w_counter._call_counter = 0
        fn_w_counter._caller_dict = {}

    caller = __name__
    fn_w_counter._call_counter += 1

    if caller in fn_w_counter._caller_dict:
        fn_w_counter._caller_dict[caller] += 1
    else:
        fn_w_counter._caller_dict[caller] = 1

    return fn_w_counter._call_counter, fn_w_counter._caller_dict
