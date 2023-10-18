custom_power = lambda x = 0, /, e = 1: x ** e

def custom_equation(x:int = 0, y:int = 0, /, a:int = 1, b:int = 1, *, c:int = 1) -> float:
    """
    This function returns the sum of two exponential expressions divided by an integer.

    :param x: First base number
    :param y: Second base number
    :param a: First exponent
    :param b: Second exponent
    :param c: Divisor
    :return: x to the power of a plus y to the power of b, divided by c
    """
    
    if c == 0:
        raise ZeroDivisionError("c cannot be zero.")
    
    return (x ** a + y ** b) / c

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "called_times"):
        fn_w_counter.called_times = 0
        fn_w_counter.caller_info = {}
    
    caller = globals().get('__name__')

    if caller:
        fn_w_counter.called_times += 1
        fn_w_counter.caller_info[caller] = fn_w_counter.caller_info.get(caller, 0) + 1

    return fn_w_counter.called_times, fn_w_counter.caller_info
