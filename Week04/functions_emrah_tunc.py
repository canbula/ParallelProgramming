custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    This function solves a specific mathematical equation.

    :param x: The base for the first exponentiation (positional-only)
    :param y: The base for the second exponentiation (positional-only)
    :param a: The exponent for x (positional-or-keyword)
    :param b: The exponent for y (positional-or-keyword)
    :param c: The divisor (keyword-only)
    :return: The result of the calculation
    """
    return float((x ** a + y ** b) / c)

def fn_w_counter(caller: str = "Unknown") -> tuple[int, dict]:
       
    
    if not hasattr(fn_w_counter, "total_call"):
        fn_w_counter.total_call = 0          
        
    if not hasattr(fn_w_counter, "caller_dict"):
        fn_w_counter.caller_dict = {}   

    fn_w_counter.total_call += 1

    if caller in fn_w_counter.caller_dict:
        fn_w_counter.caller_dict[caller] += 1
        
    else:
        fn_w_counter.caller_dict[caller] = 1

    return fn_w_counter.total_call, fn_w_counter.caller_dict
