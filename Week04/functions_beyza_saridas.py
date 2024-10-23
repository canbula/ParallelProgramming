custom_power = lambda x, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the result of the equation (x**a + y**b) / c.

    :param x: Positional-only integer, default 0
    :param y: Positional-only integer, default 0
    :param a: Positional or keyword integer, default 1
    :param b: Positional or keyword integer, default 1
    :param c: Keyword-only integer, default 1
    :return: Float result of the equation
    """
    return (x**a + y**b) / c

def fn_w_counter():
    if not hasattr(fn_w_counter, 'counter'):
        fn_w_counter.counter = 0
        fn_w_counter.callers = {}

    fn_w_counter.counter += 1
    caller_name = __name__

    if caller_name not in fn_w_counter.callers:
        fn_w_counter.callers[caller_name] = 0
    
    fn_w_counter.callers[caller_name] += 1

    return fn_w_counter.counter, fn_w_counter.callers
