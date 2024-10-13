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


counter = {}
total_calls = 0

def fn_w_counter() -> tuple[int, dict[str, int]]:
    """
    Tracks the number of calls and caller information.

    :return: A tuple with the total call count and a dictionary
             of caller names and their call counts.
    """
    global total_calls
    total_calls += 1
    counter[__name__] = counter.get(__name__, 0) + 1
    return total_calls, counter

# Örnek kullanım
for _ in range(10):
    fn_w_counter()
