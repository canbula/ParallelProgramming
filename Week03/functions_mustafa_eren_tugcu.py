from collections import defaultdict


custom_power = lambda x = 0 , e = 1, /: x**e 

def custom_equation(x = 0, y = 0, /, a = 1 , b = 1 , * , c  = 1 ):
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
    :return: x to the power of a, adds y to the power of b, then divides this sum by c
    """
    return float((x**a + y **b ) / c)


def fn_w_counter():
    caller_count = defaultdict(int)
    total_calls = 0
    
    def inner_function(caller_name):
        nonlocal total_calls
        caller_count[caller_name] += 1
        total_calls += 1
        
    return inner_function, lambda: (total_calls, dict(caller_count))
