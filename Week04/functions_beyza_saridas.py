custom_power = lambda x=0, /, e=1: x**e

def custom_equation(
    x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1
) -> float:
    """
    This function calculates (x**a + y**b) / c.

    :param int x: First variable, defaults to 0
    :param int y: Second variable, defaults to 0
    :param int a: Power of x, defaults to 1
    :param int b: Power of y, defaults to 1
    :param int c: Denominator, defaults to 1
    :return: Result of the equation (x**a + y**b) / c
    :rtype: float
    :raises ZeroDivisionError: if c is 0
    """
    return (x**a + y**b) / c

from collections import defaultdict

def fn_w_counter() -> tuple[int, dict[str, int]]:
    if not hasattr(fn_w_counter, "_counter"):
        fn_w_counter._counter = 0
        fn_w_counter._caller_count = defaultdict(int)
    
    fn_w_counter._counter += 1
    fn_w_counter._caller_count[__name__] += 1
    
    return fn_w_counter._counter, dict(fn_w_counter._caller_count)
