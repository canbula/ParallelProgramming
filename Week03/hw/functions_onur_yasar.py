custom_power = lambda x = 0, /, e = 1: x ** e

def custom_equation(x:int = 0, y:int = 0, /, a:int = 1, b:int = 1, *, c:int = 1) -> float:
    """
    This function calculates the result of adding two exponential expressions and then dividing the sum by an integer.
    :param x: First number
    :param y: Second number
    :param a: Exponent of first number
    :param b: Exponent of second number
    :param c: Divisor
    :return: x to the power of a plus y to the power of b the total divided by c
    """

    if c == 0:
        raise ZeroDivisionError()

    return (x ** a + y ** b) / c

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "called_times"):
        fn_w_counter.called_times = 0
        fn_w_counter.caller_info = {}

    caller_name = globals()['__name__']

    if caller_name:
        fn_w_counter.called_times += 1
        fn_w_counter.caller_info[caller_name] = fn_w_counter.caller_info.get(caller_name, 0) + 1

    return fn_w_counter.called_times, fn_w_counter.caller_info