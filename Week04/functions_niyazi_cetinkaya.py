custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, /, y: int = 0, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculate the result of the equation: (x**a + y**b) / c.

    :param x: positional-only integer, default is 0
    :param y: positional-only integer, default is 0
    :param a: positional-or-keyword integer, default is 1
    :param b: positional-or-keyword integer, default is 1
    :param c: keyword-only integer, default is 1
    :return: float result of the equation
    """
    return (x**a + y**b) / c

def fn_w_counter():
    """
    A function that tracks and counts the number of calls, 
    and records the caller's information.
    
    :return: Tuple containing total number of calls and a dictionary 
             with the caller's __name__ as key and the count of calls as value.
    """
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
        fn_w_counter.callers = {}
    
    fn_w_counter.call_count += 1
    caller_name = __name__
    
    if caller_name in fn_w_counter.callers:
        fn_w_counter.callers[caller_name] += 1
    else:
        fn_w_counter.callers[caller_name] = 1
    
    return fn_w_counter.call_count, fn_w_counter.callers
