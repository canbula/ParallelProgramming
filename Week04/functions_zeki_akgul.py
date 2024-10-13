custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(x:int=0, y:int=0 , / ,a:int=1,b:int=1,*,c:int=1) -> float:
    """
    "The function raises x to the power of a and y to the power of b, then adds the results together and divides the sum by c."
   
    :param x: Positional-only base value for the first term; defaults to 0.
    :param y: Positional-only base value for the second term; defaults to 0.
    :param a: Exponent for `x`, can be used as positional or keyword; defaults to 1.
    :param b: Exponent for `y`, can be used as positional or keyword; defaults to 1.
    :param c: Keyword-only divisor for the result; defaults to 1.
        
    :return: The result of the equation `(x**a + y**b) / c`.
    :rtype: float
    """
    return (x**a + y**b) / c
 

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
        fn_w_counter._dict = {}
    caller_name = __name__
    fn_w_counter.call_count += 1
    if caller_name in fn_w_counter._dict:
        fn_w_counter._dict[caller_name] += 1
    else:
        fn_w_counter._dict[caller_name] = 1
    return fn_w_counter.call_count, fn_w_counter._dict 
