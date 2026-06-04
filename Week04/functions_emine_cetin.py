custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the equation (x**a + y**b) / c.

    :param x: Base for the first term (positional only)
    :param y: Base for the second term (positional only)
    :param a: Exponent for the first term
    :param b: Exponent for the second term
    :param c: Divisor (keyword only)
    :return: The result as a float
    """
    if not all(isinstance(arg, int) for arg in [x, y, a, b, c]):
        raise TypeError("All arguments must be integers.")

    return float((x ** a + y ** b) / c)

_call_count = 0

def fn_w_counter() -> (int, dict[str, int]):
    global _call_count
    _call_count += 1
  
    return _call_count, {__name__: _call_count}
