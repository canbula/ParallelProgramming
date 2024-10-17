
custom_power = lambda x = 0, /, e = 1: x**e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates (x**a + y**b) / c
    :param x: base of the first term
    :param y: base of the second term
    :param a: power of the first term
    :param b: power of the second term
    :param c: constant divisor
    :return: result of (x**a + y**b) / c
    """
    return (x**a + y**b) / c


def fn_w_counter() -> (int, dict[str, int]):
    if hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count += 1
    else:
        fn_w_counter.call_count = 1
    if hasattr(fn_w_counter, "callers_dict"):
        if __name__ in fn_w_counter.callers_dict:
            fn_w_counter.callers_dict[__name__] += 1
        else:
            fn_w_counter.callers_dict[__name__] = 1
    else:
        fn_w_counter.callers_dict = {f"{__name__}": 1}
    return fn_w_counter.call_count, fn_w_counter.callers_dict


