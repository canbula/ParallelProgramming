custom_power = lambda x=0, /, e=1: x ** e
"""
fn = lambda arg1,arg2: arg1+arg2
"""


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculate a custom equation based on the parameters provided.

    This function computes the result of the equation:
    \((x^a + y^b) / c\), where:
    - `x` and `y` are the bases for exponentiation.
    - `a` and `b` are the exponents for `x` and `y`, respectively.
    - `c` serves as the divisor, which cannot be zero.

    :param x:
        The base for exponentiation (positional only). Default is 0.

    :param y:
        The base for exponentiation (positional only). Default is 0.

    :param a:
        The exponent for `x` (positional or keyword). Default is 1.
        This defines the power to which `x` is raised.

    :param b:
        The exponent for `y` (positional or keyword). Default is 1.
        This defines the power to which `y` is raised.

    :param c:
        A keyword-only parameter representing the divisor. Default is 1.
        If set to zero, a division by zero exception is raised.

    :raises ValueError:
        If `c` is zero, a `ValueError` is raised indicating that division by zero
        is not allowed.

    :returns:
        The result of the equation \((x^a + y^b) / c\).
        This will return a float value representing the computed result.

    :example:

    #>>> custom_equation(2, 3, a=2, b=2, c=1)
    13.0
    #>>> custom_equation(2, 3, a=2, b=2, c=0)
    Traceback (most recent call last):
        ...
    ValueError: Division by Zero Exception
    """
    if c == 0:
        raise ValueError("Division by Zero Exception")

    return (x ** a + y ** b) / c


def fn_w_counter():
    """
    A function that counts how many times it has been called and tracks callers.

    Each time this function is invoked, it increments a call counter and logs
    the name of the caller (the module name). This can be useful for debugging
    purposes or monitoring how frequently this function is used in different
    parts of the application.

    :returns:
        A tuple containing:
        - The total number of times the function has been called across all instances.
        - A dictionary mapping caller names (module names) to the number of times
          they have invoked this function.

    :example:

    #>>> fn_w_counter()
    (1, {'__main__': 1})
    #>>> fn_w_counter()
    (2, {'__main__': 2})
    """
    if not hasattr(fn_w_counter, 'call_count'):
        fn_w_counter.call_count = 0
        fn_w_counter.callers = {}
    fn_w_counter.call_count += 1

    caller_name = __name__

    if caller_name in fn_w_counter.callers:
        fn_w_counter.callers[caller_name] += 1
    else:
        fn_w_counter.callers[caller_name] = 1
    return fn_w_counter.call_count, fn_w_counter.callers
