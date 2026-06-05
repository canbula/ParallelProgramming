import inspect

custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    return (x ** a + y ** b) / c


def fn_w_counter() -> tuple[int, dict[str, int]]:

    # Get the caller's module name
    frame = inspect.stack()[1]
    caller_name = frame[0].f_globals.get("__name__", "__unknown__")

    # Update call counts
    fn_w_counter._total += 1
    fn_w_counter._callers[caller_name] = fn_w_counter._callers.get(caller_name, 0) + 1

    return (fn_w_counter._total, dict(fn_w_counter._callers))

fn_w_counter._total = 0
fn_w_counter._callers = {}
