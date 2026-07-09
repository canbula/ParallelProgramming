power_fn = lambda base=0, /, exp=1: base ** exp


def calc_expression(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates (x^a + y^b) / c
    """
    result = (x ** a + y ** b) / c
    return result


def call_tracker() -> tuple[int, dict[str, int]]:
    if not hasattr(call_tracker, "_count"):
        call_tracker._count = 0
        call_tracker._by_caller = {}

    module_name = __name__

    call_tracker._count += 1

    if module_name in call_tracker._by_caller:
        call_tracker._by_caller[module_name] += 1
    else:
        call_tracker._by_caller[module_name] = 1

    return call_tracker._count, call_tracker._by_caller
