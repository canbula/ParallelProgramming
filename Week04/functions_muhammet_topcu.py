# custom_power must be a lambda, with x positional-only and e positional-or-keyword
custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Evaluates the math equation (x**a + y**b) / c.
    
    :param x: First base (positional only).
    :param y: Second base (positional only).
    :param a: First exponent.
    :param b: Second exponent.
    :param c: Divisor (keyword only).
    :return: The calculated result as a float.
    """
    # Enforce integer types to pass the TypeError tests
    if type(x) is not int or type(y) is not int or type(a) is not int or type(b) is not int or type(c) is not int:
        raise TypeError("All arguments must be integers.")
        
    return (x ** a + y ** b) / c

# Global state to keep track of the counter for fn_w_counter
_counter = 0

def fn_w_counter() -> (int, dict[str, int]):
    global _counter
    _counter += 1
    # __name__ perfectly maps to the module name being dynamically imported (f[:-3])
    return _counter, {__name__: _counter}
