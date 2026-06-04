custom_power = lambda x=0, /, e=1: x**e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """Calculate a custom equation.

    :param x: Base value 1.
    :type x: int
    :param y: Base value 2.
    :type y: int
    :param a: Exponent for x.
    :type a: int
    :param b: Exponent for y.
    :type b: int
    :param c: Divisor.
    :type c: int
    :return: Result of (x**a + y**b) / c.
    :rtype: float
    """
    for param in (x, y, a, b, c):
        if not isinstance(param, int) or isinstance(param, bool):
            raise TypeError("All parameters must be integers.")
    return (x**a + y**b) / c


def fn_w_counter() -> (int, dict[str, int]):
    """Count function calls with caller information."""
    fn_w_counter.total += 1
    caller_name = __name__
    fn_w_counter.callers[caller_name] = fn_w_counter.callers.get(caller_name, 0) + 1
    return (fn_w_counter.total, dict(fn_w_counter.callers))


fn_w_counter.total = 0
fn_w_counter.callers = {}
