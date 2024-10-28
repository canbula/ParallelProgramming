custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:

    return (x ** a + y ** b) / c


def fn_w_counter() -> (int, dict[str, int]):

    if not hasattr(fn_w_counter, "count"):
        setattr(fn_w_counter, "count", 0)
        setattr(fn_w_counter, "caller_dict", {})

    fn_w_counter.count += 1
    caller = __name__

    if caller not in fn_w_counter.caller_dict:
        fn_w_counter.caller_dict[caller] = 0

    fn_w_counter.caller_dict[caller] += 1

    return (int(fn_w_counter.count), dict(fn_w_counter.caller_dict))