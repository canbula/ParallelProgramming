def custom_power(x=0, /, e=1):
    return e: x ** e  # Direct calculation

def custom_equation(x: int = 0, /, y: int = 0,  a: int = 1, b: int = 1, *, c: int = 1) -> float:
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
    
    return wrapper  # Return the function
