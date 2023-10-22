custom_power = lambda x = 0,e = 1 : pow(x,e)

def custom_equation(x: int = 0 ,y: int = 0,/, a: int=1, b:int=1,*,c:int = 1) -> float:
    """
    This function returns sum of squares of x and y divided by c
    :param x: First number
    :param y: Second number
    :param a: Power of first number
    :param b: Power of second number
    :param c: Divider
    :return: sum of power of x and power of y divided by c
    """
    return (x**a + y**b) / c


def fn_w_counter():
    if not hasattr(fn_w_counter, "call_counter"):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_counts = {}

    caller_name = globals().get("__name__", "__main__")
    fn_w_counter.call_counter += 1

    if caller_name in fn_w_counter.caller_counts:
        fn_w_counter.caller_counts[caller_name] += 1
    else:
        fn_w_counter.caller_counts[caller_name] = 1

    return fn_w_counter.call_counter, fn_w_counter.caller_counts











