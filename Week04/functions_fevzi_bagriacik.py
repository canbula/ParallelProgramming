custom_power = lambda x=0, /, e=1 : x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    This function calculates (x ** a + y ** b) / c 
    
    :param arg1: First number (positional-only). Default to 0.
    :param arg2: Second number (positional-only). Default to 0.
    :param arg3: Third number (positional or keyword). Default to 1.
    :param arg4: Fourth number (positional or keyword). Default to 1.
    :param arg5: Fifth number (keyword-only). Default to 1.
    :return: (x ** a + y ** b) / c.
    """
    
    return (x ** a + y ** b) / c
    
def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, 'total_count'):
        fn_w_counter.total_count = 0
        fn_w_counter.caller_dict = {}

    caller_name = fn_w_counter.__module__

    fn_w_counter.total_count += 1

    if caller_name in fn_w_counter.caller_dict:
        fn_w_counter.caller_dict[caller_name] += 1
    else:
        fn_w_counter.caller_dict[caller_name] = 1

    return fn_w_counter.total_count, fn_w_counter.caller_dict
