custom_power = lambda x = 0, /, e = 1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    This function takes x to the power of a, y to the power of b, adds x and y, divides the result to c.

    :param x: First positional-only integer
    :param y: Second positional-only integer
    :param a: First positional-or-keyword integer
    :param b: Second positional-or-keyword integer
    :param c: First keyword-only integer
    :return: (xᵃ + yᵇ) ÷ c
    """
    return (x**a + y**b) / c

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "calls"):
        fn_w_counter.calls = {}
    if __name__ not in fn_w_counter.calls:
        fn_w_counter.calls[__name__] = 0
    fn_w_counter.calls[__name__] += 1
    return (sum(fn_w_counter.calls.values()), {__name__: fn_w_counter.calls[__name__]})

