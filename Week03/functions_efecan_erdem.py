custom_power = lambda x = 0, /, e = 1: x**e

def custom_equation(x: int = 0, y:int= 0, /, a:int=1, b:int=1, *, c:int= 1) -> float:
    """
    This function performs calculation using the given parameters

    :param x: First integer, positional-only (default: 0)
    :param y: Second integer, positional-only (default: 0)
    :param a: First exponent (default: 1)
    :param b: Second exponent (default: 1)
    :param c: Divisor, keyword-only (default: 1)
    :return: (x**a + y**b) / c  -> float
    """
    return float((x**a + y**b) / c)

def fn_w_counter() ->(int, dict[str, int]):
    """
    This function returns a tuple that includes who called it, how many times it has been called, and the total call count
    :return: (total_call_count, {caller_function_name: call_count})
    """
    if not hasattr(fn_w_counter, 'counter'):
       fn_w_counter.counter = 1
       fn_w_counter.caller= {}
    else:
       fn_w_counter.counter += 1
    if __name__ not in fn_w_counter.caller:
       fn_w_counter.caller[__name__] = 1
    else:
       fn_w_counter.caller[__name__] += 1

    return fn_w_counter.counter, fn_w_counter.caller