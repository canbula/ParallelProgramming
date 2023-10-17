from collections import defaultdict 
import inspect

custom_power = (lambda x=0, /, e=1 : x**e)


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Compute the result of the expression: (x**a + y**b) / c).

    :param x: The base for the first exponentiation (default 0).
    :param y: The base for the second exponentiation (default 0).
    :param a: The exponent for the first term (default 1).
    :param b: The exponent for the second term (default 1).
    :param c: The divisor for the final expression (default 1).
    :return: The computed result as a float.

    :Example:

    >>> custom_function(2, 3, 2, 2, 2)
    12.5
    """
    
    return float((x ** a + y ** b) / c)


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
