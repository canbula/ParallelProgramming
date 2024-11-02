custom_power = lambda x=0, /, e=1: x**e
"""
A lambda function that raises x to the power of e.

:param x: The positional-only integer base parameter for the power calculation, default is 0.
:param e: The positional-or-keyword integer exponent parameter for the power calculation, default is 1.
:return: The result of x raised to the power of e.
:rtype: int
"""

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculate a custom equation with specified base, exponent, and divisor values.

    :param x: The positional-only integer base parameter for the equation, default is 0.
    :param y: The positional-only integer base parameter for the equation, default is 0.
    :param a: The positional-or-keyword integer exponent parameter for x, default is 1.
    :param b: The positional-or-keyword integer exponent parameter for y, default is 1.
    :param c: The keyword-only integer divisor parameter for the equation, default is 1.
    :return: The result of the calculation as a float, computed as (x**a + y**b) / c.
    :rtype: float
    """
    return (x**a + y**b) / c

def fn_w_counter() -> tuple[int, dict[str, int]]:
    """
    Track and return the number of function calls and caller information.

    This function maintains an internal counter and a dictionary to record
    how many times it has been called from each caller. It returns the
    total number of calls and a dictionary with caller names as keys
    and their respective call counts as values.

    :return: A tuple where the first element is the total number of calls (int),
             and the second element is a dictionary with caller names as keys
             and the number of calls from each caller as values.
    :rtype: tuple[int, dict[str, int]]
    """
    if not hasattr(fn_w_counter, '_call_counter'):
        fn_w_counter._call_counter = 0
        fn_w_counter._caller_dict = {}
    caller = __name__
    fn_w_counter._call_counter += 1
    if caller in fn_w_counter._caller_dict:
        fn_w_counter._caller_dict[caller] += 1
    else:
        fn_w_counter._caller_dict[caller] = 1
    return fn_w_counter._call_counter, fn_w_counter._caller_dict
