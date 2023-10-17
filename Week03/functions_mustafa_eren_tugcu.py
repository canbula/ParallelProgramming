from collections import defaultdict
from typing import Tuple, Dict

custom_power = lambda x = 0 , / ,e = 1, : x**e 

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1 ) -> float :
    """
    This function raises x to the power of a, 
    adds y to the power of b, 
    then divides this sum by c, 
    and returns the result as a floating-point number.
    
    :param x : First Number 
    :param y : Second Number 
    :param a : Third Number 
    :param b : Fourth Number 
    :param c : Fifth Number 
    :return: result as a floating-point number.
    """
    return float((x**a + y **b ) / c)

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "call_counter"):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_counts = {}

    caller_name = __name__
    fn_w_counter.call_counter += 1

    if caller_name in fn_w_counter.caller_counts:
        fn_w_counter.caller_counts[caller_name] += 1
    else:
        fn_w_counter.caller_counts[caller_name] = 1

    return fn_w_counter.call_counter, fn_w_counter.caller_counts

    
