custom_power = lambda x=0, /, e=1: x**e

def custom_equation(x: int=0, y: int=0, /, a: int=1, b: int=1, *, c: int=1) -> float:
    """
    Compute the result of the expression: (x**a + y**b) / c).
    :param x: First positional-only integer (default 0)
    :param y: Second positional-only integer (default 0)
    :param a: First positional-or-keyword integer (default 1)
    :param b: Second positional-or-keyword integer (default 1)
    :param c: First keyword-only integer (default 1)
    :return: (x**a + y**b) / c)
    """
    return (x**a + y**b) / c

def fn_w_counter() -> (int,dict[str,int]):
    caller_name = __name__
    if not hasattr(fn_w_counter,"call_counter"):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_counts = {}
    fn_w_counter.call_counter += 1
    if caller_name in fn_w_counter.caller_counts:
        fn_w_counter.caller_counts[caller_name] += 1
    else:
        fn_w_counter.caller_counts[caller_name] = 1
    return  fn_w_counter.call_counter, fn_w_counter.caller_counts
