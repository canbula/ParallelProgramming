"""
    Musa Sina ERTUGRUL 200316011

    This homework has been done for understanding
    functions in Python at week 3. Also, rest 
    docstring format has been used in this file.

"""

custom_power = lambda x = 0, /,e = 1 : x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1 ) -> float :
    """
    Calculate the result of a custom equation.

    :param x (int): The base value for the 'x' parameter.
    :param y (int): The base value for the 'y' parameter.
    :param a (int): The exponent for the 'x' parameter.
    :param b (int): The exponent for the 'y' parameter.
    :param c (int): The divisor for the result.

    :return float: The result of the custom equation (x^a + y^b) / c.
    """
    return (x**a+y**b)/c

def fn_w_counter()->(int,dict[str,int]):
    """
    Track function call count and who called the function.

    This function keeps track of the number of times it has been called
    and maintains a dictionary to record which functions have called it.

    Returns:
    Tuple[int, Dict]: A tuple containing the call count (int) and a dictionary
    (Dict) showing the count of calls from different functions.
    """

    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
    if not hasattr(fn_w_counter,"who_called"):
        fn_w_counter.who_called = {__name__ : 0}

    fn_w_counter.call_count += 1
    if not fn_w_counter.who_called[__name__]:
        fn_w_counter.who_called[__name__] = 1
    else:
        fn_w_counter.who_called[__name__] += 1

    return (fn_w_counter.call_count,fn_w_counter.who_called)

