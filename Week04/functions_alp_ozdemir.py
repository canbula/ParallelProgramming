custom_power = lambda x = 0, / ,e = 1 : x**e 

def custom_equation(x : int  = 0,y : int = 0,/,a : int = 1,b: int = 1,*,c: int = 1) -> float:
    
    """
    Calculates the mathematical equation.

    :param x: The first base value.
    :param y: The second base value.
    :param a: The exponent for x.
    :param b: The exponent for y.
    :param c: The divisor.
    :return: The result of the equation.
    """

    res = float((x ** a + y**b) / c)
    return res

def fn_w_counter() -> (int,dict[str,int]):
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = 0
    fn_w_counter.counter += 1
    return fn_w_counter.counter, {__name__: fn_w_counter.counter}
   
