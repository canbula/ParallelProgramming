def custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculate the result of the equation (x**a + y**b) / c.

    :param x: Positional-only integer with default value 0
    :param y: Positional-only integer with default value 0
    :param a: Positional-or-keyword integer with default value 1
    :param b: Positional-or-keyword integer with default value 1
    :param c: Keyword-only integer with default value 1
    :return: A float that is the result of the equation (x**a + y**b) / c
    """
    return (x**a + y**b) / c

def fn_w_counter():
    fn_w_counter.counter += 1
    if not hasattr(fn_w_counter, 'call_dict'):
        fn_w_counter.call_dict = {}

    caller = '__main__'
    if caller in fn_w_counter.call_dict:
        fn_w_counter.call_dict[caller] += 1
    else:
        fn_w_counter.call_dict[caller] = 1

    return fn_w_counter.counter, fn_w_counter.call_dict

