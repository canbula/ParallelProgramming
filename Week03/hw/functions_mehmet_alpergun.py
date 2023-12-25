custom_power = lambda x = 0,/,e = 1: x**e
"""
this function take a power of a number
:param x: a number which is taken power
:param e: a numer which is power
:return: takes a power(e) of a number(x)
"""

def custom_equation(x: int = 0,y: int = 0,/,a: int = 1,b: int = 1,*,c: int =1) -> float:
    """
    making custom equation
    :param x: position-only with default value 0
    :param y: position-only with default value 0
    :param a: position-or-keyword with default value 1
    :param b: position-or-keyword with default value 1
    :param c: keyword-only with default value 1
    :return: it returns float number
    """
    return (x**a + y**b)/c

def fn_w_counter()->(int,dict[str,int]):
    """
    it counts that how many calls this function anywhere
    :return: (calling number, {the function name : calling number})
    """
    caller_name = globals()['__name__']
    if not hasattr(fn_w_counter,"counter"):
        fn_w_counter.counter = 0
        fn_w_counter.caller_info = {}
    fn_w_counter.counter += 1
    

    if caller_name in fn_w_counter.caller_info:
        fn_w_counter.caller_info[caller_name] += 1
    else:
        fn_w_counter.caller_info[caller_name] = 1
    return fn_w_counter.counter, fn_w_counter.caller_info
