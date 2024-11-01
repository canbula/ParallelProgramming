custom_power = lambda x=0,/,e=1 : x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    :param x: The positional-only integer base for the first term, default is 0
    :param y: The positional-only integer base for the second term, default is 0
    :param a: The positional-or-keyword integer exponent for the first term, default is 1
    :param b: The positional-or-keyword integer exponent for the second term, default is 1
    :param c: The keyword-only integer divisor, default is 1
    :return: The result of the calculation as a float
    :rtype: float
    """
    return (x**a + y**b) / c




def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = 0
        fn_w_counter.dict = {}
    caller_name = __name__
    fn_w_counter.counter += 1
    if caller_name in fn_w_counter.dict:
        fn_w_counter.dict[caller_name] += 1
    else:
        fn_w_counter.dict[caller_name] = 1
    return fn_w_counter.counter, fn_w_counter.dict 
