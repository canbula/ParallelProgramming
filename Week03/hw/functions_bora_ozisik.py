custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
        This function takes 5 integer parameters and calculates
        the result of dividing the first parameter to the power
        of the third parameter plus the second parameter to the
        power of the fourth parameter, divided by the fifth parameter.

        It briefly means that this function calculates the following equation:

        (x^a + y^b) / c

        :param x: First integer(positional-only).
        :type x: int
        :param y: Second integer(positional-only).
        :type y: int
        :param a: Third integer(positional-or-keyword).
        :type a: int
        :param b: Fourth integer(positional-or-keyword).
        :type b: int
        :param c: Fifth integer(keyword-only).
        :type c: int
        :return: (x^a + y^b) / c.

    """

    return (x**a + y**b) / c


def fn_w_counter() -> (int, dict[str, int]):
    caller_name = __name__
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
        fn_w_counter.caller_callersCallCount_dict = {}
        """
        I used camel case for 'callersCallCount' because caller's 
        call count was a pattern word and I didn't want you to
        confuse the meaning of variable's name.
        """

    if caller_name in fn_w_counter.caller_callersCallCount_dict:
        fn_w_counter.caller_callersCallCount_dict[caller_name] += 1
    else:
        fn_w_counter.caller_callersCallCount_dict[caller_name] = 1

    fn_w_counter.call_count += 1

    return fn_w_counter.call_count, fn_w_counter.caller_callersCallCount_dict
