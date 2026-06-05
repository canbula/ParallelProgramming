import inspect


custom_power = lambda x=0, /, e=1: pow(x, e)


def custom_equation(x: int, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Compute a custom equation result.

    :param x: First base value
    :param y: Second base value
    :param a: Power for x
    :param b: Power for y
    :param c: Divider
    :return: Float result of the equation
    """
    value_x = pow(x, a)
    value_y = pow(y, b)

    combined = value_x + value_y

    if c == 0:
        return 0.0  # safe fallback (division guard)

    return float(combined / c)


def fn_w_counter() -> tuple[int, dict[str, int]]:
    if not hasattr(fn_w_counter, "_count"):
        fn_w_counter._count = 0
        fn_w_counter._call_map = {}

    caller = inspect.stack()[1].frame.f_globals.get("__name__", "__main__")

    fn_w_counter._count += 1

    fn_w_counter._call_map[caller] = fn_w_counter._call_map.get(caller, 0) + 1

    return fn_w_counter._count, fn_w_counter._call_map