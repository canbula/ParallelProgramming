# Lambda function to compute x raised to the power e
custom_power = lambda x=0, /, e=1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Computes the equation (x**a + y**b) / c.

    :param x: Base value for the first term (positional-only, defaults to 0).
    :param y: Base value for the second term (positional-only, defaults to 0).
    :param a: Exponent applied to x (default is 1).
    :param b: Exponent applied to y (default is 1).
    :param c: Divisor for the equation (keyword-only, default is 1).
    :return: The calculated result as a float.
    :raises ZeroDivisionError: If c equals 0.
    """
    if c == 0:  # Ensure we don't divide by zero
        raise ZeroDivisionError("Division by zero is not allowed.")
    
    return (x**a + y**b) / c  # Compute the result

def fn_w_counter() -> tuple[int, dict[str, int]]:
    """
    Tracks the number of function calls and the caller's name.

    :return: A tuple with the total call count and a dictionary mapping callers to their respective counts.
    """
    # Initialize attributes if they don't exist
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0  # Total call count
        fn_w_counter.callers_dict = {}  # Caller-specific counts

    # Increment total call count
    fn_w_counter.call_count += 1

    # Identify the caller's module
    caller = __name__

    # Update the caller's count
    if caller in fn_w_counter.callers_dict:
        fn_w_counter.callers_dict[caller] += 1
    else:
        fn_w_counter.callers_dict[caller] = 1

    return fn_w_counter.call_count, fn_w_counter.callers_dict
