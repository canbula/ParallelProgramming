custom_power = lambda x=0, /, e=1: x**e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    a function that takes 5 arguments, 2 of which are optional, and returns a float
    :param x: (int) first value
    :param y: (int) second value
    :param a: (int) first exponent
    :param b: (int) second exponent
    :param c: (int) divisor
    :return: (float) result of the equation
    """
    return (x**a + y**b) / c




def fn_w_counter() -> (int, dict[str, int]):
    # Get the caller's name
    caller = fn_w_counter.__name__

    # Initialize counters if they don't exist
    if not hasattr(fn_w_counter, 'call_counter'):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_counts = {}
    
    # Increment the call counter
    fn_w_counter.call_counter += 1

    # Increment the caller-specific counter
    if caller in fn_w_counter.caller_counts:
        fn_w_counter.caller_counts[caller] += 1
    else:
        fn_w_counter.caller_counts[caller] = 1

    # Return the results
    return fn_w_counter.call_counter, fn_w_counter.caller_counts
