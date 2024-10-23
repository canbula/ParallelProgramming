custom_power = lambda x=0, e=1: x ** e

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

def fn_w_counter()-> (int, dict[str, int]):
    """A function that counts the number of calls."""
    caller_name = inspect.stack()[1].function  # Get the name of the calling function

    # Increment the global counter
    call_count[caller_name] += 1

    # Calculate the total number of calls
    total_calls = sum(call_count.values())

    # Return the total call count and the call counts for each function
    return total_calls, dict(call_count)
