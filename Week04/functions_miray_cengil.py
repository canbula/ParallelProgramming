custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:

    """
    A function that calculates the custom equation:
    
    (x**a + y**b) / c
    
    :param x: positional-only integer, default 0
    :param y: positional-only integer, default 0
    :param a: positional-or-keyword integer, default 1
    :param b: positional-or-keyword integer, default 1
    :param c: keyword-only integer, default 1
    :return: Result of the equation as a float
    """
    return (x**a + y**b) / c

from collections import defaultdict
import inspect

call_count = defaultdict(int)

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "call_counter"):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_count_dict = {}

    # Get the name of the caller
    caller_name = __name__
    fn_w_counter.call_counter += 1

    # If the caller is already in the dictionary, increment its value
    if caller_name in fn_w_counter.caller_count_dict:
        fn_w_counter.caller_count_dict[caller_name] += 1
    else:
        # Otherwise, add it as a new key
        fn_w_counter.caller_count_dict[caller_name] = 1

    # Return the total call count and the caller information
    return fn_w_counter.call_counter, fn_w_counter.caller_count_dict
