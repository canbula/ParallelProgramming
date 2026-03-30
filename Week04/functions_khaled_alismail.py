import inspect


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
    Evaluate the custom equation.

    :param x: First integer base.
    :param y: Second integer base.
    :param a: Power used for ``x``.
    :param b: Power used for ``y``.
    :param c: Keyword-only divisor.
    :return: The floating-point result of ``(x**a + y**b) / c``.
    """
    return float((x ** a + y ** b) / c)


_counter_state = {
    "total": 0,
    "callers": {}
}


def fn_w_counter() -> tuple[int, dict[str, int]]:
    frame = inspect.currentframe()
    caller_frame = frame.f_back if frame else None
    caller_name = "<unknown>"

    if caller_frame is not None:
        caller_name = caller_frame.f_globals.get("__name__", "<unknown>")

    _counter_state["total"] += 1
    _counter_state["callers"][caller_name] = _counter_state["callers"].get(caller_name, 0) + 1

    return _counter_state["total"], dict(_counter_state["callers"])
