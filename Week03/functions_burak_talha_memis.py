fn = lambda arg1 , arg2 : arg1 * arg2

def custom_power(x = 0, /, e = 1):
    return x ** e

def custom_equation(x: int = 0, y: int = 0 ,/,a: int = 1,b: int = 1 ,*, c: int = 1) -> (float):
    """
    :param x: first integer with default value 0 (positional-only)
    :param y: second integer with default value 0 (positional-only)
    :param a: third integer with default value 1 (positional-or-keyword)
    :param bb: fourth integer with default value 1 (positional-or-keyword)
    :param c: fifth integer with default value 1 (keyword-only)
    :raises TypeError: if x, y, a, b or c is not an integer
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if not isinstance(y, int):
        raise TypeError("y must be an integer")
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    if not isinstance(c, int):
        raise TypeError("c must be an integer")
    return float(x ** a + y ** b) / c

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, 'counter'):
        fn_w_counter.counter = 0
    fn_w_counter.counter += 1
    if not hasattr(fn_w_counter, 'callers'):
        fn_w_counter.callers = {f"{__name__}":1}
    else:
        if __name__ in fn_w_counter.callers:
            fn_w_counter.callers[__name__] +=1
        else:
            fn_w_counter.callers[__name__] =1
    return  (fn_w_counter.counter, fn_w_counter.callers)
'''
for i in range(10):
    fn_w_counter()
print(fn_w_counter())   
''' 
