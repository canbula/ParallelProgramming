custom_power = lambda x = 0 ,/, e=1 : x**e

def custom_equation(x = 0, y = 0 , / , a = 1 , b = 1 , * ,c =1 ):
    """
    The function compute the result of the :((x**a + y**b) /c).
    :param x: First positional-only integer (default=0)
    :param y: Second positional-only integer (default=0)
    :param a: First positional-or-keyword integer (default=1)
    :param b: Second positional-or-keyword integer (default=1)
    :param c: First keyword-only integer(default=1)
    :return: ((x**a + y**b)/c)
    """
    return (x**a + y**b )/c


def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
        fn_w_counter._dict = {}
    caller_name = __name__
    fn_w_counter.call_count += 1
    if caller_name in fn_w_counter._dict:
        fn_w_counter._dict[caller_name] += 1
    else:
        fn_w_counter._dict[caller_name] = 1
    return fn_w_counter.call_count, fn_w_counter._dict
