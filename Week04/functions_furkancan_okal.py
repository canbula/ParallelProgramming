custom_power = lambda x = 0, /, e =1 : x ** e




def custom_equation(x:int = 0 , y:int = 0, /, a:int = 1, b:int = 1, *, c:int = 1) -> float:
    """
    This function calculates custom equation

    (x**a + y**b) / c

    :param x: base of exponentation of first term
    :param y: base of exponentation of second term
    :param a: exponent of first term
    :param b: exponent of second term
    :param c: divider of sum

    :return: Result of equation
    
    :raises ZeroDivisionError: if c is zero
    :raises TypeError: if parameters not numeric
    """
    return (x**a + y**b) / c

def fn_w_counter() -> (int,dict[str,int]):
    if(hasattr(fn_w_counter,"totalCount")):
        totalCount = getattr(fn_w_counter,"totalCount")
        setattr(fn_w_counter,"totalCount",totalCount+1)
        calls = getattr(fn_w_counter,"calls")
        calls.update({__name__:calls.get(__name__)+1})
    else:
        setattr(fn_w_counter,"calls",{__name__:1})
        setattr(fn_w_counter,"totalCount",1)

    return ((getattr(fn_w_counter,"totalCount"),getattr(fn_w_counter,"calls")))
