import os
 
custom_power = lambda x=0, /, e=1: x ** e
 
 
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Returns (x**a + y**b) / c.
 
    :param x: Base for the first term.
    :param y: Base for the second term.
    :param a: Exponent for x.
    :param b: Exponent for y.
    :param c: Divisor.
    :return: Result as float.
    """
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(c, int):
        raise TypeError("x, y and c must be integers")
    return (x ** a + y ** b) / c
 
 
_name = os.path.splitext(os.path.basename(__file__))[0]
_count = [0]
 
def fn_w_counter() -> (int, dict[str, int]):
    _count[0] += 1
    return (_count[0], {_name: _count[0]})
