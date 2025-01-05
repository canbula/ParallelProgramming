custom_power = lambda x=0, /, e=1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the value of the equation (x**a + y**b) / c.

    :param x: Positional-only base value for the first term; defaults to 0.
    :param y: Positional-only base value for the second term; defaults to 0.
    :param a: Exponent for x; defaults to 1.
    :param b: Exponent for y; defaults to 1.
    :param c: Keyword-only divisor for the equation; defaults to 1.
    :return: Result of the equation as a float.
    :rtype: float
    :raises ZeroDivisionError: if c is 0.
    """
    if c == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return (x**a + y**b) / c

def fn_w_counter() -> (int, dict[str, int]):
    """
    Counts the number of times it has been called and tracks the caller.

    :return: Tuple containing total call count and a dictionary with caller info.
    :rtype: tuple
    """
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
        fn_w_counter.callers_dict = {}
    
    fn_w_counter.call_count += 1
    caller = __name__
    
    if caller in fn_w_counter.callers_dict:
        fn_w_counter.callers_dict[caller] += 1
    else:
        fn_w_counter.callers_dict[caller] = 1
    
    return fn_w_counter.call_count, fn_w_counter.callers_dict
