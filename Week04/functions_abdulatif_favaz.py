import sys


custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(
    x: int = 0,
    y: int = 0,
    /,
    a: int = 1,
    b: int = 1,
    *,
    c: int = 1
) -> float:
    """
    Calculate a custom equation.

    :param x: Base value of the first term.
    :param y: Base value of the second term.
    :param a: Exponent applied to ``x``.
    :param b: Exponent applied to ``y``.
    :param c: Divisor of the final sum.
    :return: The result of ``(x**a + y**b) / c`` as a float.
    """
    return float((x ** a + y ** b) / c)


def fn_w_counter() -> tuple[int, dict[str, int]]:
    caller_name = sys._getframe(1).f_globals.get("__name__", "<unknown>")

    fn_w_counter.total_calls += 1
    fn_w_counter.callers[caller_name] = fn_w_counter.callers.get(caller_name, 0) + 1

    return fn_w_counter.total_calls, dict(fn_w_counter.callers)


fn_w_counter.total_calls = 0
fn_w_counter.callers = {}
