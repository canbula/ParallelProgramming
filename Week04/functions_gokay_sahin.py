import inspect


custom_power = lambda x = 0, /, e = 1 : x ** e


def custom_equation(x: int | float = 0, y: int | float = 0, /, a: int | float = 1, b: int | float = 1, *, c: int | float = 1) -> float:
    """
    Calculates the result of the equation (x^a + y^b) / c.

    :param x: The base for the first term (defaults to 0).
    :type x: int or float
    :param y: The base for the second term (defaults to 0).
    :type y: int or float
    :param a: The exponent for the first term (defaults to 1).
    :type a: int or float
    :param b: The exponent for the second term (defaults to 1).
    :type b: int or float
    :param c: The divisor (must not be 0, defaults to 1).
    :type c: int or float

    :raises ZeroDivisionError: Raised if `c` is 0 to prevent division by zero.

    :return: The result of the equation (x^a + y^b) / c.
    :rtype: float
    """
    if c == 0:
        raise ZeroDivisionError("Division by zero is not supported!")
    return (x**a + y**b) / c


call_count = 0
caller_dict = {}


def fn_w_counter() -> (int, dict[str, int]):
    """
    Tracks the number of times the function has been called and keeps a record of the caller module.

    This function increments a global `call_count` variable and updates a global `caller_dict` dictionary,
    which stores the number of calls made from each module.

    :return: A tuple containing the total call count and a dictionary with the module names as keys and the number of calls as values.
    :rtype: tuple(int, dict)
    """
    global call_count
    global caller_dict
    call_count += 1

    frame = inspect.currentframe()

    module_name = inspect.getmodule(frame).__name__  # __main__

    if module_name in caller_dict:
        caller_dict[module_name] += 1
    else:
        caller_dict[module_name] = 1

    return call_count, caller_dict


