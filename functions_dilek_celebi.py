# custom_power
custom_power = lambda x=0, e=1: x ** e

# custom_equation
def custom_equation(
    x: int = 0,
    y: int = 0,
    a: int = 1,
    b: int = 1,
    *,
    c: int = 1
) -> float:
    """
    A custom equation function.

    :param x: First positional integer parameter (default is 0)
    :param y: Second positional integer parameter (default is 0)
    :param a: Third integer parameter, positional-or-keyword (default is 1)
    :param b: Fourth integer parameter, positional-or-keyword (default is 1)
    :param c: Fifth integer parameter, keyword-only (default is 1)
    :return: Result of the equation (x**a + y**b) / c as a float
    """
    return (x**a + y**b) / c

# fn_w_counter
def fn_w_counter():
    """
    Counts the number of calls from each caller.

    :return: A tuple containing the total number of calls (int)
             and a dictionary with the caller's name as keys
             and the number of calls from that caller as values.
    """
    fn_w_counter.call_count += 1
    caller_name = __name__
    fn_w_counter.caller_info[caller_name] = fn_w_counter.caller_info.get(caller_name, 0) + 1
    return fn_w_counter.call_count, fn_w_counter.caller_info

# Initialize function attributes for fn_w_counter
fn_w_counter.call_count = 0
fn_w_counter.caller_info = {}
