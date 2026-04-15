import inspect

custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates (x**a + y**b) / c with specific parameter constraints.

    :param x: base for the first term (positional-only)
    :param y: base for the second term (positional-only)
    :param a: exponent for x
    :param b: exponent for y
    :param c: divisor (keyword-only)
    :return: result of the equation as a float
    """
    if not all(isinstance(val, int) for val in [x, y, a, b, c]):
        raise TypeError("Parameters must be integers")
    
    return float((x**a + y**b) / c)

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "count"):
        fn_w_counter.count = 0
        fn_w_counter.callers = {}

    fn_w_counter.count += 1
    
    caller_frame = inspect.currentframe().f_back
    caller_name = caller_frame.f_globals.get('__name__', 'unknown')
    
    fn_w_counter.callers[caller_name] = fn_w_counter.callers.get(caller_name, 0) + 1
    
    return fn_w_counter.count, fn_w_counter.callers
