custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    This function takes 5 parameters and returns (x**a+y**b)/c equation as a float value.

    :param x: first integer, positional only
    :param y: second integer, positional only
    :param a: first exponent, positional or keyword
    :param b: second exponent, positional or keyword
    :param c: denominator, keyword only
    :return: float
    """
    return (x ** a + y ** b) / c


def fn_w_counter() -> (int, dict[str, int]):
    """
    This function counts the number of calls with caller information.

    :return: (int, dict[str, int])
    """
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
        fn_w_counter.calls = {}

    if (__name__ not in fn_w_counter.calls):
        fn_w_counter.calls[__name__] = 0

    fn_w_counter.calls[__name__] += 1
    fn_w_counter.call_count += 1
    return fn_w_counter.call_count, fn_w_counter.calls
