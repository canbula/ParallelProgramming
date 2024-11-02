# custom_power
def custom_power(x=0, e=1):
    """
    Calculates x raised to the power of e with default values.
    
    :param x: Base number (default is 0)
    :param e: Exponent (default is 1)
    :return: Result of x raised to the power of e
    """
    return x ** e

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
    Computes the equation (x^a + y^b) / c with specified parameters.
    
    :param x: First number, default is 0
    :param y: Second number, default is 0
    :param a: Power for x, default is 1
    :param b: Power for y, default is 1
    :param c: Divisor, default is 1, keyword-only
    :return: Result of the calculation as a float
    """
    return (x ** a + y ** b) / c

# fn_w_counter
def fn_w_counter():
    """
    Tracks the total number of calls to this function and counts calls by each caller.

    :return: A tuple with the total call count and a dictionary of caller names with their counts.
    """
    fn_w_counter.call_count += 1
    caller = fn_w_counter.__name__
    fn_w_counter.caller_counts[caller] = fn_w_counter.caller_counts.get(caller, 0) + 1
    return fn_w_counter.call_count, fn_w_counter.caller_counts

# Initialize tracking variables for fn_w_counter
fn_w_counter.call_count = 0
fn_w_counter.caller_counts = {}
