def custom_power(x=0, /, e=1):
    """
    A lambda function that takes two parameters, x and e, and returns x to the power of e.
    
    :param x: positional-only parameter (default 0)
    :param e: positional-or-keyword parameter (default 1)
    :return: x raised to the power of e
    """
    return lambda e: x ** e

def custom_equation(x: int = 0, /, y: int = 0,  a: int = 1, b: int = 1, *, c: int = 1) -> float:
    return (x**a + y**b) / c

from collections import defaultdict

call_count = defaultdict(int)

def fn_w_counter():
    """
    A function that counts the number of calls and returns a tuple.
    
    The first element is the total number of calls.
    The second element is a dictionary with caller information (caller __name__ and count).
    
    :return: A tuple of an integer and a dictionary
    """
    def wrapper():
        import inspect
        caller_name = inspect.stack()[1].function
        call_count[caller_name] += 1
        total_calls = sum(call_count.values())
        return total_calls, dict(call_count)
    
    return wrapper
