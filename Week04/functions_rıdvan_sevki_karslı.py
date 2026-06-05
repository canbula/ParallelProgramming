custom_power = lambda x=0, /, e=1: pow(x, e)


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Computes a custom equation.
    
    :param x: First base (positional only)
    :param y: Second base (positional only)
    :param a: First exponent
    :param b: Second exponent
    :param c: Divisor (keyword only)
    :return: The result of (x^a + y^b) / c
    """

    params = {'x': x, 'y': y, 'a': a, 'b': b, 'c': c}
    
    for param_name in params:
        if type(params[param_name]) is not int:
            raise TypeError(f"{param_name} must be an integer")

    if c == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    result = (custom_power(x, a) + custom_power(y, b)) / c

    return float(result)


def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "count"):
        setattr(fn_w_counter, "count", 0)

    setattr(fn_w_counter, "count", fn_w_counter.count + 1)

    return fn_w_counter.count, {fn_w_counter.__name__: fn_w_counter.count}
