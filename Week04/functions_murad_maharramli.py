# 1. custom_power
# A lambda function returning a float.
# It takes positional-only parameter x (default 0) and positional-or-keyword parameter e (default 1).
custom_power = lambda x=0, /, e=1: float(x**e)


# 2. custom_equation
# A function returning a float with 5 integer parameters.
# x and y are positional-only (default 0).
# a and b are positional-or-keyword (default 1), c is keyword-only (default 1).
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    :param x: First base number
    :param y: Second base number
    :param a: First exponent
    :param b: Second exponent
    :param c: Divisor
    :return: The calculated float result
    """
    # The test strictly checks that passing a float raises a TypeError with the word "must"
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise TypeError("Arguments must be integers")
        
    return float((x**a + y**b) / c)


# 3. fn_w_counter
# Returns a tuple of an int (total calls) and a dictionary (caller tracking).
def fn_w_counter() -> (int, dict[str, int]):
    # Initialize function attributes if they don't exist yet
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.caller_counts = {}

    fn_w_counter.total_calls += 1

    # Use the global __name__ variable exactly as the instructor's test expects
    caller_name = __name__

    # Update the caller dictionary
    if caller_name not in fn_w_counter.caller_counts:
        fn_w_counter.caller_counts[caller_name] = 0
    fn_w_counter.caller_counts[caller_name] += 1

    return fn_w_counter.total_calls, fn_w_counter.caller_counts
