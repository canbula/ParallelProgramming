import inspect


custom_power = lambda x = 0, /, e = 1 : x ** e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the result of the equation (x^a + y^b) / c.

    :param x: The base for the first term (defaults to 0).
    :type x: int
    :param y: The base for the second term (defaults to 0).
    :type y: int
    :param a: The exponent for the first term (defaults to 1).
    :type a: int
    :param b: The exponent for the second term (defaults to 1).
    :type b: int
    :param c: The divisor (must not be 0, defaults to 1).
    :type c: int

    :raises ZeroDivisionError: Raised if `c` is 0 to prevent division by zero.

    :return: The result of the equation (x^a + y^b) / c.
    :rtype: float
    """
    if c == 0:
        raise ZeroDivisionError("Division by zero is not supported!")
    return (x**a + y**b) / c



def fn_w_counter() -> (int, dict[str, int]):
    """
    Tracks the number of times the function is called and keeps a count of calls per module.

    This function increments a counter each time it is called and stores the number of calls 
    per module in a dictionary. The counter is stored as a function attribute and is initialized 
    on the first call. The module name from which the function is called is tracked using the 
    `inspect` module.

    :returns: 
        - A tuple where the first value is the total number of calls made to the function, 
          and the second value is a dictionary containing the count of calls per module.
        - The dictionary keys are module names, and the values are the corresponding call counts.

    :rtype: tuple(int, dict[str, int])
    """
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
        fn_w_counter.caller_dict = {}

    fn_w_counter.call_count += 1

    frame = inspect.currentframe()

    module_name = inspect.getmodule(frame).__name__  # __main__

    if module_name in fn_w_counter.caller_dict:
        fn_w_counter.caller_dict[module_name] += 1
    else:
        fn_w_counter.caller_dict[module_name] = 1

    return fn_w_counter.call_count, fn_w_counter.caller_dict
