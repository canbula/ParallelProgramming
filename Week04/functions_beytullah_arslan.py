custom_power = lambda x = 0 , / , e = 1 : x**e

def custom_equation(x: int = 0 , y: int = 0 , / , a: int = 1 , b: int = 1 , * , c: int = 1 ) -> float:
    """
   This function calculates a custom equation with the given five integers.

    :param x: First base value
    :param y: Second base value
    :param a: Exponent of variable x
    :param b: Exponent of variable y
    :param c: Divisor value
    :return: The float result of the operation
    """

    return (x**a + y**b) / c

def fn_w_counter() -> tuple[int, dict[str, int]]:
    if not hasattr(fn_w_counter,'call_counter'):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_dict = {}
    caller = __name__
    fn_w_counter.call_counter += 1
    if caller in fn_w_counter.caller_dict:
        fn_w_counter.caller_dict[caller] += 1
    else:
        fn_w_counter.caller_dict[caller] = 1
    return fn_w_counter.call_counter,fn_w_counter.caller_dict

