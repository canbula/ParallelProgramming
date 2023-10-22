custom_power = lambda x = 0 , / ,e = 1 : x ** e

def custom_equation(x = 0, y = 0, / , a = 1, b = 1, * , c = 1) -> float:
    """
    Calculate the result of a custom equation:
    :param x: number 1
    :param y: number 2
    :param a: exponent of number 1
    :param b: exponent of number 2
    :param c: number 3
    :return:  compute the result of (x**a + y**b) divided by c.
    """
    return (x**a + y**b) / c


def fn_w_counter() -> (int, dict[str, int]):
    """
        Counts function calls and tracks caller modules.

        Returns:
            Tuple: (call_count, caller_dict)

        - call_count: Total number of times this function has been called.
        - caller: Dictionary of caller module names and their call counts.
    """

    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
        fn_w_counter.caller = {}
    caller_name = __name__
    fn_w_counter.call_count += 1
    if caller_name in fn_w_counter.caller:
        fn_w_counter.caller[caller_name] += 1
    else:
        fn_w_counter.caller[caller_name] = 1
    return fn_w_counter.call_count, fn_w_counter.caller



