custom_power = lambda x=0,/,e=1 : x**e
"""
This lambda function calculates the power of a number.

:param x: The base number (default is 0, positional-only).
:param e: The exponent (default is 1).
:return: The result of x raised to the power of e.
"""

def custom_equation(x: int = 0, y: int = 0,/, a: int = 1, b: int = 1,*, c: int = 1) -> float:
    """
    This function calculates the result of (x raised to the power of a) plus (y raised to the power of b),
    divided by c.

    :param x: The first number (default is 0, positional-only).
    :param y: The second number (default is 0, positional-only).
    :param a: The exponent for x (default is 1).
    :param b: The exponent for y (default is 1).
    :param c: The divisor (default is 1, keyword-only).
    :return: The result of (x**a + y**b) / c.
    """
    return (x**a + y**b) / c


def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = (0, {})
    counter_num = fn_w_counter.counter[0]
    counter_dict = fn_w_counter.counter[1]
    if __name__ in counter_dict:
        counter_dict[__name__] += 1
    else:
        counter_dict[__name__] = 1
    fn_w_counter.counter = (counter_num + 1, counter_dict)
    return fn_w_counter.counter
