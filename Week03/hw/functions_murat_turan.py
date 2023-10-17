custom_power = lambda x = 0 , / ,e = 1, : x**e 

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    
    """
    Calculate (x^a + y^b) / c.

    :param x:  First base, positional-only, default 0.
    :param y:  Second base, positional-only, default 0.
    :param a:  Exponent for x, positional-or-keyword, default 1.
    :param b:  Exponent for y, positional-or-keyword, default 1.
    :param c:  Divisor, keyword-only, default 1.

    :return: (float) Result of the calculation.
    """
    return float((x ** a + y ** b) / c)

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "call_counter"):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_counts = {}
    caller_name = __name__
    fn_w_counter.call_counter += 1
    if caller_name in fn_w_counter.caller_counts:
        fn_w_counter.caller_counts[caller_name] += 1
    else:
        fn_w_counter.caller_counts[caller_name] = 1
    return fn_w_counter.call_counter, fn_w_counter.caller_counts
