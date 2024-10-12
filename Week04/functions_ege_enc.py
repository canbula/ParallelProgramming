custom_power = lambda x=0, /, e=1 : x**e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculate a custom equation based on the given parameters.

    The equation calculates (x*a + y*b) / c.

    :param x: Positional-only integer, base number, default is 0.
    :param y: Positional-only integer, base number, default is 0.
    :param a: Exponent applied to x, default is 1.
    :param b: Exponent applied to y, default is 1.
    :param c: Keyword-only integer, divisor, default is 1.

    :return: The result of the equation as a float.
    """
    return (x*a + y*b) / c
    
    
    
def fn_w_counter() -> tuple[int,dict]:
    """
    Count the number of times the function is called and track caller information.
    
    :return: A tuple containing the total number of calls (int) and a dictionary
             with caller names as keys and the number of calls from each caller as values.
    """
   
    counter = 0
    caller_info = {}

    def wrapped_function():
        nonlocal counter  
        counter += 1
        caller_name = _name_  
        
        if caller_name in caller_info:
            caller_info[caller_name] += 1  
       
        else:
            caller_info[caller_name] = 1
            
        return counter, caller_info

    return wrapped_function
