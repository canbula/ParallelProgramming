custom_power = lambda x=0, /, e=1 : x**e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculate a custom equation based on the given parameters.

    The equation calculates (x**a + y**b) / c.

    :param x: Positional-only integer, base number, default is 0.
    :param y: Positional-only integer, base number, default is 0.
    :param a: Exponent applied to x, default is 1.
    :param b: Exponent applied to y, default is 1.
    :param c: Keyword-only integer, divisor, default is 1.

    :return: The result of the equation as a float.
    """
    return (x**a + y**b) / c
    
    
    
def fn_w_counter() -> tuple[int, dict[str, int]]:
    """
    This function tracks the total number of calls and records how many times 
    each caller (using __name__) invokes it.
    
    It keeps track of:
      - total number of calls (counter)
      - a dictionary (caller_info) where the key is the caller name (str) and the value 
        is the number of times that caller has invoked the function (int).
    
    :return: A tuple containing:
      - an integer (total number of calls)
      - a dictionary with caller names as keys (str) and the number of times 
        they've called the function as values (int).
    """
    if not hasattr(fn_w_counter, 'counter'):
        fn_w_counter.counter = 0
        fn_w_counter.caller_info = {}

    fn_w_counter.counter += 1
    
    caller_name = __name__ 
    
    if caller_name in fn_w_counter.caller_info:
        fn_w_counter.caller_info[caller_name] += 1
    else:
        fn_w_counter.caller_info[caller_name] = 1

    return int(fn_w_counter.counter), fn_w_counter.caller_info
