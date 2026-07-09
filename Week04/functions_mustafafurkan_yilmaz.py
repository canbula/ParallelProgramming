# 1. custom_power: A lambda function that raises x to the power of e
custom_power = lambda x=0, /, e=1: x ** e

# 2. custom_equation: Implements (x^a + y^b) / c
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
    # Type checking to satisfy the "must" message requirement in TypeError
    if not all(isinstance(arg, int) for arg in [x, y, a, b, c]):
        raise TypeError("All arguments must be integers.")

    return float((x ** a + y ** b) / c)

# 3. fn_w_counter: A stateful function tracking how many times it is called
# We use a global variable to maintain the state across calls.
_call_count = 0

def fn_w_counter() -> (int, dict[str, int]):
    global _call_count
    _call_count += 1
    # Returns the current count and a dict mapping the module name to the count
    return _call_count, {__name__: _call_count}
