from collections import defaultdict 
import inspect

custom_power = (lambda x=0, /, e=1 : x**e)


def custom_function(x = 0, y = 0, /, a = 1, b = 1, *, c = 1) -> float:
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


    def fn_w_counter():
        caller_count = defaultdict(int)
        total_calls = 0

        def inner_function():
            nonlocal total_calls
            caller_name = inspect.stack()[1].frame.f.globals['__name__']
            caller_count[caller_name] +=1
            total_calls +=1
            return total_calls, caller_count

        return inner_function
