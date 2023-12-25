
custom_power = lambda x = 0 , / , e = 1 : x**e


def custom_equation(x:int=0, y:int=0 , / ,a:int=1,b:int=1,*,c:int=1) -> float:
    """
    This function takes the power of two numbers and divides their sum by a number.
    :param x: First number
    :param y: Second number
    :param a: Third number
    :param b: Fourth number
    :param c: Fifth number
    :return (x**a+y**b)/c
    """
    return (x**a+y**b)/c



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
