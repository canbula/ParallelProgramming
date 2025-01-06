custom_power = lambda x=0, /, e=1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Compute a custom equation.
    :param x: Positional-only base for the first term (default: 0)
    :param y: Positional-only base for the second term (default: 0)
    :param a: Exponent for the first term (default: 1)
    :param b: Exponent for the second term (default: 1)
    :param c: Divisor, keyword-only (default: 1)
    :return: Result of the calculation as a float
    """
    if c == 0:  # Ensure we don't divide by zero
        raise ZeroDivisionError("Division by zero is not allowed.")
    return (x**a + y**b) / c

def fn_w_counter() -> tuple[int, dict]:
    """
    Function that tracks how many times it has been called and logs calls by module name.
    :return: A tuple containing the call count and a dictionary of module call statistics.
    """
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = 0
        fn_w_counter.dict = {}
    caller_name = __name__
    fn_w_counter.counter += 1
    fn_w_counter.dict[caller_name] = fn_w_counter.dict.get(caller_name, 0) + 1
    return fn_w_counter.counter, fn_w_counter.dict
