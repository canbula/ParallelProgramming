def custom_power(x: int = 0, y: int = 0, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the equation (x**a + y**b) / c.

    :param x: Positional-only integer, default is 0.
    :param y: Positional-only integer, default is 0.
    :param a: Positional-or-keyword integer, default is 1.
    :param b: Positional-or-keyword integer, default is 1.
    :param c: Keyword-only integer, default is 1.
    :returns: Result of the equation (x**a + y**b) / c as float.
    """
    return (x ** a + y ** b) / c



def custom_equation(x: int = 0, y: int = 0, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the equation (x**a + y**b) / c.

    :param x: Positional-only integer, default is 0.
    :param y: Positional-only integer, default is 0.
    :param a: Positional-or-keyword integer, default is 1.
    :param b: Positional-or-keyword integer, default is 1.
    :param c: Keyword-only integer, default is 1.
    :returns: Result of the equation (x**a + y**b) / c as float.
    """
    return (x ** a + y ** b) / c


call_count = 0
callers = {}

def fn_w_counter() -> tuple[int, dict]:
    """
    Counts the number of times the function is called
    and tracks the caller information.

    :returns: Tuple of (number of calls, dictionary of caller counts).
    """
    global call_count, callers
    call_count += 1
    caller_name = __name__
    
    if caller_name in callers:
        callers[caller_name] += 1
    else:
        callers[caller_name] = 1

    return call_count, callers
