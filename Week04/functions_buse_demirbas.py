def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates (x**a + y**b) / c with specific parameter rules.

    :param x: Positional-only base x
    :param y: Positional-only base y
    :param a: Positional-or-keyword exponent a
    :param b: Positional-or-keyword exponent b
    :param c: Keyword-only divisor c
    :return: The result of the equation as float
    """
    if not all(isinstance(i, int) for i in [x, y, a, b, c]):
        raise TypeError("All parameters must be integers")
    
    return float((x**a + y**b) / c)

custom_power = lambda x=0, /, e=1: x**e

_counter = 0
_call_map = {}

def fn_w_counter() -> tuple[int, dict[str, int]]:
    global _counter
    _counter += 1
    module_name = __name__.split('.')[-1] 
    _call_map[module_name] = _counter
    return _counter, _call_map
