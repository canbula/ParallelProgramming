custom_power = lambda x = 0,/,e = 1: x**e
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *,c: int) -> float:
    """
    Takes arguments in the correct order and format according to the specified parameter types and calculates the sum of two numbers raised to powers, then divides the result by a third number.

    :param x: The base for the exponentiation operation and positional-only. Default value is 0.
    :type x: int, float
    :param y: The base for the exponentiation and operation positional-only. Default value is 0.
    :type y: int, float
    :param a: The exponent for the x value anf positional-or-Keyword . Default value is 1.
    :type a: int
    :param b: The exponent for the y value and positional-or-Keyword. Default value is 1.
    :type b: int
    :param c: The number by which the total result of the exponentiation sum will be divided and Keyword-Only This is a required parameter.
    :type c: int, float
    :return: Returns the result of the expression (x^a + y^b) / c.
    :rtype: float
    :raises ZeroDivisionError: Raises this error if c is zero.

    Example:

    .. code-block:: python

        result = custom_equation(3, 5, a=2, b=3, c=4)
        print(result)  # Output: 33.5
    """
    return (x ** a + y ** b) / c

counter = 0
dict_ = {}
def fn_w_counter():
    global counter
    counter +=1
    caller_function_name = __name__
    if caller_function_name in dict_:
        dict_[caller_function_name] +=1
    else:
        dict_[caller_function_name] =1
    result_list = [counter,dict_]
    return tuple(result_list)














