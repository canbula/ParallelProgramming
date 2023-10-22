custom_power = lambda x = 0, /, e = 1 : x**e

def custom_equation(x: int = 0 , y: int = 0 , / , a:int = 1, b: int = 1, * , c: int = 1) -> float:
    """
    This function adds the b power of the y variable to the a power of the x variable. Divides the result by variable c.
    
    :param x: First base number
    :param y: Second base number
    :param a: First exponent
    :param b: Second exponent
    :param c: Divisior number
    :return: Returns the result of the equation as a float
    """
    return (x**a + y**b) / c


def fn_w_counter() -> (int, dict[str,int]):
    """ 
    This function counts the number of calls and returns with caller information.

    :return : (total number of calls, {caller function name: number of calls})
    """
    
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = 0
        fn_w_counter.caller_info = {}
        
    caller_name = __name__
    fn_w_counter.counter += 1
    
    if caller_name in fn_w_counter.caller_info:
        fn_w_counter.caller_info[caller_name] += 1
    else:
        fn_w_counter.caller_info[caller_name] = 1
        
    return (fn_w_counter.counter, fn_w_counter.caller_info)   
