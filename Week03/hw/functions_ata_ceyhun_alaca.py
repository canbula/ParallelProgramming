custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    This function finds the sum of 'x' raised to power of 'a' and 'y' raised to power of 'b' afterwards, divides this sum with 'c'.
    :param x: First number
    :param y: Second number
    :param a: Third number
    :param b: Fourth number
    :param c: Fifth number
    :return: Resulting value.
    """
    return float((x**a + y**b) / c)

def fn_w_counter() -> (int, dict[str, int]):
    """
    A function that counts how many times it is called while keeping a record of which module called it how many times.
    :return: call count and names of the called.
    """
    if not hasattr(fn_w_counter, 'count'):
        fn_w_counter.count = 0
    fn_w_counter.count += 1
    if not hasattr(fn_w_counter, 'caller_names'):
        fn_w_counter.caller_names = {f"{__name__}": 1}
    else:
        if __name__ in fn_w_counter.caller_names:
            fn_w_counter.caller_names[__name__] += 1
        else:
            fn_w_counter.caller_names[__name__] = 1
    return fn_w_counter.count, fn_w_counter.caller_names

