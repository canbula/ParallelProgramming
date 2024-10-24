custom_power = lambda x=0,/, e=1 :  x ** e

def custom_equation(x:int = 0, y:int = 0,/, a:int = 1, b:int = 1,*,c:int=1)->float:
    """
    Computes a custom equation based on the given parameters.

    The equation is defined as: (x**a + y**b) / c

    :param x : The base value for the first term, default is 0.
    :param y : The base value for the second term, default is 0.
    :param a : The exponent for the first term, default is 1.
    :param b : The exponent for the second term, default is 1.
    :param c : The divisor for the equation, default is 1.
    :return  : The result of the custom equation.
    """
    return (x**a + y**b) / c


def fn_w_counter()->(int, dict[str,int]):
    """
    This function tracks how many times it has been called and returns this count,
    along with the name of the module from which it was called.

    :return: A tuple containing the current call count (int) and a dictionary 
             where the module name (str) is the key and the call count (int) is the value.
    """
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = 0
    fn_w_counter.counter += 1
    module_name = __name__
    call_counter_dict = {module_name: fn_w_counter.counter}
    
    return fn_w_counter.counter, call_counter_dict

