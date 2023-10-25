custom_power = lambda x = 0, /, e = 1: x ** e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    This function calculates the result of adding two exponential expressions and then dividing the sum by an integer.
    :param x: First number
    :param y: Second number
    :param a: Exponent of first number
    :param b: Exponent of second number
    :param c: Divisor
    :return: x to the power of a plus y to the power of b the total divided by c
    """
    return (x ** a + y ** b) / c


def fn_w_counter() -> (int, dict[str, int]):
    """
    This function counts how many times it is called and by which caller.
    :return: Total call count and caller info
    """
    if not hasattr(fn_w_counter, "number_of_calls"):
        fn_w_counter.number_of_calls = 0
        fn_w_counter.caller_info = {}

    fn_w_counter.number_of_calls += 1
    fn_w_counter.caller_info[__name__] = fn_w_counter.caller_info.get(
        __name__, 0) + 1

    return fn_w_counter.number_of_calls, fn_w_counter.caller_info
