custom_power = lambda x=0, /, e=1 : print(x**e)

def custom_equation(x: int = 0, y: int = 0, / , a: int = 1, b: int = 1, * , c: int = 1) -> float:
    """
    This function returns the summation of x prime a and y prime b divided by c as a float.

    :param x: First number as a positional-only integer
    :param y: Second number as a positional-only integer
    :param a: Third number as a positional-or-keyword integer
    :param b: Fourth number as a positional-or-keyword integer
    :param c: Fifth number as a keyword-only integer
    :return: Float type value of the result of that summation of x prime a and y prime b divided by c
    """
    return (x**a + y**b)/c


def fn_w_counter() -> (int, {str : int}):
    if not hasattr(fn_w_counter,"theDict"):
        fn_w_counter.theTotalCalls = 0
        fn_w_counter.theDict = dict({})

    fn_w_counter.theTotalCalls += 1

    tempCaller = __name__
    if not tempCaller in fn_w_counter.theDict:
        fn_w_counter.theDict[tempCaller] = 1
    else:
        fn_w_counter.theDict.update({tempCaller : fn_w_counter.theDict[tempCaller] + 1})
    
    return fn_w_counter.theTotalCalls, fn_w_counter.theDict
