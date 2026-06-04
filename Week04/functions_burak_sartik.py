custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the mathematical equation.

    :param x: The first base value.
    :type x: int
    :param y: The second base value.
    :type y: int
    :param a: The exponent for x.
    :type a: int
    :param b: The exponent for y.
    :type b: int
    :param c: The divisor.
    :type c: int
    :return: The result of the equation.
    :rtype: float
    """
    return (x**a + y**b) / c

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "count"):
        fn_w_counter.count = 0

    fn_w_counter.count += 1

    module_name = __name__.split('.')[-1]

    return fn_w_counter.count, {module_name: fn_w_counter.count}

