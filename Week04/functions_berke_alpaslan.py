custom_power = lambda x = 0, /, e = 1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculate a custom equation based on the provided parameters.

    The function computes the result of the equation:
    (x**a + y**b) / c

    :param x: The first integer value (positional-only, default is 0).
    :param y: The second integer value (positional-only, default is 0).
    :param a: The exponent for x (positional or keyword, default is 1).
    :param b: The exponent for y (positional or keyword, default is 1).
    :param c: The divisor (keyword-only, default is 1).
    :return: The result of the equation as a float.
    """
    return (x**a + y**b) / c

call_counter = 0
caller_count_dict = {}
def fn_w_counter() -> (int, dict[str, int]):
    global call_counter
    global caller_count_dict

    caller = __name__
    call_counter += 1

    if caller not in caller_count_dict:
        caller_count_dict[caller] = 1
    else:
        caller_count_dict[caller] += 1

    return call_counter, caller_count_dict
