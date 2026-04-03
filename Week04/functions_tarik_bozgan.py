custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    :param x:
    :param y:
    :param a:
    :param b:
    :param c:
    :return:
    """
    if not isinstance(x, int): raise TypeError("x must be int")
    if not isinstance(y, int): raise TypeError("y must be int")
    if not isinstance(a, int): raise TypeError("a must be int")
    if not isinstance(b, int): raise TypeError("b must be int")
    if not isinstance(c, int): raise TypeError("c must be int")
    
    return float((x ** a + y ** b) / c)

_count = 0
def fn_w_counter() -> (int, dict[str, int]):
    global _count
    _count += 1
    return _count, {__name__: _count}
