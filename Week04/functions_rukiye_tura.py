custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:

    if c == 0:
        raise ValueError("Division by Zero Exception")

    return (x ** a + y ** b) / c

def fn_w_counter() -> (int, dict[str, int]):
    
    if not hasattr(fn_w_counter, 'call_count'):
        fn_w_counter.call_count = 0
        fn_w_counter.callers = {}
    fn_w_counter.call_count += 1

    caller_name = __name__

    if caller_name in fn_w_counter.callers:
        fn_w_counter.callers[caller_name] += 1
    else:
        fn_w_counter.callers[caller_name] = 1
    return fn_w_counter.call_count, fn_w_counter.callers
