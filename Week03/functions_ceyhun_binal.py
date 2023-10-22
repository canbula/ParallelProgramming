custom_power = lambda x=0,/,e=1: x**e
"""
this function take a power of a number
:param x: a number which is taken power
:param e: a numer which is power
:return: takes a power(e) of a number(x)
"""

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, c: int = 1) -> float:
    """
    Calculate a custom equation and return the result as a float.

    :param x: Positional-only integer parameter (default 0).
    :param y: Positional-only integer parameter (default 0).
    :param a: Positional-or-keyword integer parameter (default 1).
    :param b: Positional-or-keyword integer parameter (default 1).
    :param c: Keyword-only integer parameter (default 1).

    :return: Result of (x**a + y**b) / c as a float.
    """
    result = (x**a + y**b) / c
    return float(result)

def fn_w_counter()->(int,dict[str,int]):
    """
    Count the number of calls with caller information and return a tuple.

    :return: A tuple containing the total number of calls and a dictionary
             with caller (__name__) as key and the number of calls from that caller as value.
    :rtype: tuple[int, dict]
    """
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = 0
        fn_w_counter.caller_info = {}
        
    caller_name = __name__
    fn_w_counter.counter += 1
    
    if caller_name in fn_w_counter.caller_info:
        fn_w_counter.caller_info[caller_name] += 1
    else:
        fn_w_counter.caller_info[caller_name] = 1
        
    return (fn_w_counter.counter, fn_w_counter.caller_info)   
